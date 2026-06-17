/**
 * api.js — HTTP client for all backend API calls + demo mode fallback
 */

'use strict';

const API = (() => {

  // ── Core fetch wrapper ────────────────────────────────────────
  async function request(method, path, body = null, signal = null) {
    const base = APP_CONFIG.getBackendUrl();
    if (!base) throw new Error('DEMO_MODE');

    const url = `${base}${path}`;
    const opts = {
      method,
      headers: { 'Content-Type': 'application/json' },
      signal,
    };
    if (body !== null) opts.body = JSON.stringify(body);

    const resp = await fetch(url, opts);

    if (!resp.ok) {
      let msg = `HTTP ${resp.status}`;
      try { const j = await resp.json(); msg = j.detail || j.message || msg; } catch {}
      throw new Error(msg);
    }

    if (resp.status === 204) return null;
    return resp.json();
  }

  async function GET(path, params = {})      { const q = new URLSearchParams(params).toString(); return request('GET', q ? `${path}?${q}` : path); }
  async function POST(path, body, signal)    { return request('POST', path, body, signal); }
  async function PUT(path, body)             { return request('PUT', path, body); }
  async function PATCH(path, body)           { return request('PATCH', path, body); }
  async function DELETE(path)               { return request('DELETE', path); }

  // ── Upload helper (multipart) ─────────────────────────────────
  async function uploadFile(file, onProgress) {
    const base = APP_CONFIG.getBackendUrl();
    if (!base) throw new Error('DEMO_MODE');

    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();
      const fd  = new FormData();
      fd.append('file', file);

      xhr.upload.addEventListener('progress', e => {
        if (e.lengthComputable && onProgress) onProgress(Math.round(e.loaded / e.total * 100));
      });
      xhr.addEventListener('load', () => {
        if (xhr.status >= 200 && xhr.status < 300) {
          try { resolve(JSON.parse(xhr.responseText)); }
          catch { resolve({ success: true }); }
        } else {
          reject(new Error(`Upload failed: HTTP ${xhr.status}`));
        }
      });
      xhr.addEventListener('error', () => reject(new Error('Upload network error')));
      xhr.addEventListener('timeout', () => reject(new Error('Upload timed out')));

      xhr.open('POST', `${base}/api/admin/upload`);
      xhr.timeout = 120_000;
      xhr.send(fd);
    });
  }

  // ── Connection test ───────────────────────────────────────────
  async function testConnection(url) {
    const cleanUrl = (url || '').replace(/\/$/, '');
    try {
      const resp = await fetch(`${cleanUrl}/health`, { method: 'GET', signal: AbortSignal.timeout(6000) });
      if (!resp.ok) return { ok: false, msg: `HTTP ${resp.status}` };
      const json = await resp.json().catch(() => ({}));
      return { ok: true, msg: json.status || 'Connected', version: json.version };
    } catch (e) {
      return { ok: false, msg: e.message || 'Connection failed' };
    }
  }

  // ── Chat API ──────────────────────────────────────────────────
  async function sendMessage(sessionId, message, signal) {
    return POST('/api/chat', { session_id: sessionId, message }, signal);
  }

  async function getChatHistory(sessionId) {
    return GET(`/api/chat/history/${sessionId}`);
  }

  async function submitRating(messageId, rating) {
    return POST('/api/chat/rating', { message_id: messageId, rating });
  }

  // ── Forms API ─────────────────────────────────────────────────
  async function getForm(formId)      { return GET(`/api/forms/${formId}`); }
  async function listForms()          { return GET('/api/forms'); }
  async function submitForm(formId, data, sessionId) {
    return POST('/api/forms/submit', { form_id: formId, data, session_id: sessionId });
  }

  // ── Admin – Documents ─────────────────────────────────────────
  async function getDocuments()           { return GET('/api/admin/documents'); }
  async function deleteDocument(docId)    { return DELETE(`/api/admin/documents/${docId}`); }
  async function reindexDocuments()       { return POST('/api/admin/reindex', {}); }

  // ── Admin – Analytics ─────────────────────────────────────────
  async function getAnalytics(days = 30) { return GET('/api/admin/analytics', { days }); }

  // ── Admin – Conversations ─────────────────────────────────────
  async function getConversations(page = 1, search = '') {
    return GET('/api/admin/conversations', { page, limit: 20, search });
  }

  // ── Admin – Config ────────────────────────────────────────────
  async function saveConfig(settings) { return PUT('/api/admin/config', settings); }
  async function getConfig()          { return GET('/api/admin/config'); }

  // ── Demo mode data generators ─────────────────────────────────
  const DEMO_RESPONSES = [
    "Thanks for reaching out! Based on what you've asked, here's what I can tell you: we offer a wide range of products including electronics, home goods, and clothing. Our catalog is updated weekly with new arrivals.",
    "Great question! Our standard shipping typically takes 3–5 business days. We also offer express (1–2 days) and overnight options at checkout. Free shipping on orders over $50!",
    "I'd be happy to help with your return! Our return policy allows returns within 30 days of purchase for most items. Simply visit your order history, select the item, and click 'Start Return'. We'll email you a prepaid label.",
    "To track your order, you can visit the 'My Orders' section after logging in, or use the tracking number from your shipping confirmation email on our tracking page. Orders usually ship within 1–2 business days.",
    "We currently have a fantastic sale on electronics — up to 40% off select laptops and tablets! Our newest collection of wireless headphones just arrived too. Would you like me to narrow down recommendations based on your needs?",
    "Our customer support team is available Monday–Friday 9am–6pm EST, and Saturday 10am–4pm. You can reach them at support@shopbot.ai or via our live chat. For urgent matters, our phone line is 1-800-SHOPBOT.",
    "For wholesale or bulk orders, please contact our B2B team at wholesale@shopbot.ai. We offer special pricing for orders of 50+ units and can provide custom invoicing for business accounts.",
    "I don't have specific information about that right now. I'd recommend reaching out to our support team who can give you the most up-to-date details. Would you like help with something else I can assist with?",
  ];

  // Demo intent detection (mirrors backend logic)
  function detectDemoIntent(message) {
    const lower = message.toLowerCase();
    const intents = [
      {
        formId: 'tile_quote',
        keywords: ['quote', 'quotation', 'price', 'pricing', 'how much', 'cost', 'estimate', 'get a quote', 'need a quote', 'quote for tiles', 'tile prices', 'what does it cost'],
      },
      {
        formId: 'contact_me',
        keywords: ['contact me', 'call me', 'phone me', 'get in touch', 'speak to someone', 'talk to a person', 'call back', 'speak to sales', 'speak to consultant', 'human', 'representative'],
      },
      {
        formId: 'store_assistance',
        keywords: ['visit store', 'come to store', 'book appointment', 'in-store', 'showroom', 'see products', 'look at tiles', 'visit branch', 'booking', 'appointment'],
      },
      {
        formId: 'product_enquiry',
        keywords: ['product enquiry', 'looking for', 'do you have', 'stock', 'availability', 'where can i find', 'do you sell'],
      },
      {
        formId: 'sample_request',
        keywords: ['sample', 'samples', 'tile sample', 'free sample', 'get samples', 'request sample'],
      },
      {
        formId: 'contractor_quote',
        keywords: ['contractor', 'trade quote', 'trade price', 'bulk order', 'builder', 'developer', 'interior designer', 'architect'],
      },
    ];

    for (const intent of intents) {
      for (const kw of intent.keywords) {
        if (lower.includes(kw.toLowerCase())) {
          return intent.formId;
        }
      }
    }
    return null;
  }

  function getDemoResponse(message) {
    const lower = message.toLowerCase();

    // Check for form-triggering intents FIRST
    const formId = detectDemoIntent(message);
    if (formId) {
      const formMessages = {
        tile_quote: "I'd be happy to help you with a quote! Please complete the form below and one of our team members will get back to you with a tailored estimate.",
        contact_me: "No problem — we'll have someone from our team contact you. Please fill in your details below and we'll be in touch shortly.",
        store_assistance: "Great idea — visiting a showroom is the best way to see our ranges. Please let us know your preferred branch and we'll arrange assistance for you.",
        product_enquiry: "Let me help you find the right product. Please provide a few details below and our product specialist will assist you.",
        sample_request: "We'd be happy to send you samples! Please complete the request below — you can request up to 5 different tile samples.",
        contractor_quote: "Thank you for your interest in our trade services. Please complete the contractor quote form below and our trade team will assist you with competitive pricing.",
      };
      return {
        response: formMessages[formId] || 'Please complete the form below.',
        type: 'form',
        form_id: formId,
        message_id: APP_CONFIG.generateSessionId(),
      };
    }

    if (lower.includes('ship') || lower.includes('deliver')) return DEMO_RESPONSES[1];
    if (lower.includes('return') || lower.includes('refund') || lower.includes('exchange')) return DEMO_RESPONSES[2];
    if (lower.includes('track') || lower.includes('order status')) return DEMO_RESPONSES[3];
    if (lower.includes('sale') || lower.includes('deal') || lower.includes('discount') || lower.includes('product') || lower.includes('offer')) return DEMO_RESPONSES[4];
    if (lower.includes('contact') || lower.includes('support') || lower.includes('help') || lower.includes('phone')) return DEMO_RESPONSES[5];
    if (lower.includes('bulk') || lower.includes('wholesale') || lower.includes('business')) return DEMO_RESPONSES[6];
    if (lower.includes('what
