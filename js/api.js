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

  // ── Chat with images ────────────────────────────────────────
  async function sendMessageWithImages(sessionId, message, imageFiles, signal) {
    if (APP_CONFIG.isDemoMode()) return demoSendMessage(message);

    const base = APP_CONFIG.getBackendUrl();
    const formData = new FormData();
    formData.append("session_id", sessionId);
    if (message) formData.append("message", message);
    imageFiles.forEach(file => formData.append("images", file));

    const resp = await fetch(`${base}/api/chat/with-images`, {
      method: "POST",
      body: formData,
      signal,
    });

    if (!resp.ok) {
      let msg = `HTTP ${resp.status}`;
      try { const j = await resp.json(); msg = j.detail || j.message || msg; } catch {}
      throw new Error(msg);
    }
    return resp.json();
  }

  // ── Forms ─────────────────────────────────────────────────────
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

  // Demo intent detection — CONSERVATIVE (mirrors backend logic)
  // Only triggers on clear action requests, NEVER on info queries
  function detectDemoIntent(message) {
    const lower = message.toLowerCase();
    const intents = [
      {
        formId: 'get_quote',
        keywords: ['quote', 'quotation', 'get a quote', 'need a quote', 'how much', 'what does it cost', 'price for', 'pricing on', 'sample', 'samples', 'tile sample', 'free sample', 'contractor', 'trade price', 'trade quote', 'bulk order', 'need pricing', 'send me a quote', 'want a quote'],
      },
      {
        formId: 'get_in_touch',
        keywords: ['contact me', 'call me', 'call me back', 'get in touch', 'speak to someone', 'talk to a person', 'speak to sales', 'human', 'representative', 'someone call me', 'visit showroom', 'book appointment', 'come to store', 'showroom visit', 'want to visit', 'book a consultation', 'pop in', 'drop by'],
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
        get_quote: "I'd be happy to help with that! Please leave your details below and one of our team will get back to you with a quote.",
        get_in_touch: "No problem — we'll have someone from our team contact you. Please leave your details below and we'll be in touch shortly.",
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
    if (lower.includes('what') && lower.includes('offer')) return DEMO_RESPONSES[0];
    return DEMO_RESPONSES[Math.floor(Math.random() * DEMO_RESPONSES.length)];
  }

  async function demoSendMessage(message) {
    await new Promise(r => setTimeout(r, 900 + Math.random() * 1200));
    const result = getDemoResponse(message);

    const responseText = typeof result === 'string' ? result : result.response;
    const isFormTrigger = typeof result === 'object' && result.type === 'form';

    const convs = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, []);
    convs.push({
      id: APP_CONFIG.generateSessionId(),
      session_id: APP_CONFIG.getOrCreateSession(),
      user_message: message,
      bot_response: responseText,
      timestamp: new Date().toISOString(),
      rating: null,
    });
    if (convs.length > 200) convs.splice(0, convs.length - 200);
    APP_CONFIG.set(APP_CONFIG.KEYS.CONVERSATIONS, convs);

    const an = APP_CONFIG.get(APP_CONFIG.KEYS.ANALYTICS, { queries: 0, totalTime: 0 });
    an.queries = (an.queries || 0) + 1;
    an.totalTime = (an.totalTime || 0) + (900 + Math.random() * 1200);
    APP_CONFIG.set(APP_CONFIG.KEYS.ANALYTICS, an);

    const msgId = APP_CONFIG.generateSessionId();
    if (isFormTrigger) {
      return { response: result.response, type: 'form', form_id: result.form_id, message_id: msgId, sources: [] };
    }
    return { response: responseText, type: 'text', message_id: msgId, sources: [] };
  }

  // ── Unified chat (auto demo fallback) ─────────────────────────
  async function chat(message, sessionId, signal) {
    if (APP_CONFIG.isDemoMode()) return demoSendMessage(message);
    return sendMessage(sessionId, message, signal);
  }

  return {
    GET, POST, PUT, PATCH, DELETE,
    uploadFile,
    testConnection,
    // Chat
    chat,
    chatWithImages: sendMessageWithImages,
    sendMessage,
    sendMessageWithImages,
    getChatHistory,
    submitRating,
    // Forms
    getForm,
    listForms,
    submitForm,
    // Documents
    getDocuments,
    deleteDocument,
    reindexDocuments,
    // Analytics
    getAnalytics,
    // Conversations
    getConversations,
    // Config
    saveConfig,
    getConfig,
    // Demo
    demoSendMessage,
  };
})();

window.API = API;