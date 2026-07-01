/**
 * main.js — Entry point for the chat page (index.html)
 * Initialises all modules and handles backend config modal.
 */

'use strict';

(async function initApp() {

  // ── Boot sequence ─────────────────────────────────────────────
  THEME.init();
  CHAT.init();

  // ── Backend config modal ──────────────────────────────────────
  // NOTE (Phase 1 customer-facing cleanup): This modal is developer/
  // admin tooling only. It is left fully intact and functional below
  // (reversible), but nothing on the public page opens it any more —
  // the old "Configure" banner button has been replaced with a
  // customer-friendly "Request Help" button that opens the existing
  // lead-capture form instead (handled further down).
  const configModal     = document.getElementById('config-modal');
  const backendUrlInput = document.getElementById('backend-url-input');
  const saveConfigBtn   = document.getElementById('save-config');
  const cancelConfigBtn = document.getElementById('cancel-config');
  const closeConfigBtn  = document.getElementById('close-config-modal');
  const requestHelpBtn  = document.getElementById('request-help-btn');
  const connBanner      = document.getElementById('connection-banner');
  const connMsg         = document.getElementById('connection-msg');

  // Friendly, non-technical fallback message shown to customers only
  // when the backend is genuinely unreachable (not during normal
  // cold-start delays, which stay silent as before).
  const FRIENDLY_CONNECTION_MSG =
    "Tori is taking a little longer than usual to connect. Please try again in a moment, or leave your details and our team will assist.";

  // Pre-fill saved URL
  if (backendUrlInput) {
    backendUrlInput.value = APP_CONFIG.getBackendUrl() || '';
  }

  function openConfigModal() {
    if (!configModal) return;
    if (backendUrlInput) backendUrlInput.value = APP_CONFIG.getBackendUrl() || '';
    configModal.classList.remove('hidden');
    setTimeout(() => backendUrlInput?.focus(), 100);
  }

  function closeConfigModal() {
    configModal?.classList.add('hidden');
  }

  // The public page no longer exposes a button that opens this modal.
  // (openConfigModal/closeConfigModal are kept for admin/dev use and
  // remain callable from the browser console if ever needed.)
  cancelConfigBtn?.addEventListener('click', closeConfigModal);
  closeConfigBtn?.addEventListener('click', closeConfigModal);
  configModal?.addEventListener('click', e => {
    if (e.target === configModal) closeConfigModal();
  });

  // Save backend URL + test connection
  saveConfigBtn?.addEventListener('click', async () => {
    const url = (backendUrlInput?.value || '').trim();
    saveConfigBtn.disabled = true;
    saveConfigBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Testing…';

    if (!url) {
      // Demo mode
      APP_CONFIG.setBackendUrl('');
      closeConfigModal();
      TOAST.show('Running in demo mode', 'info');
      updateConnectionBanner();
      saveConfigBtn.disabled = false;
      saveConfigBtn.innerHTML = '<i class="fas fa-save"></i> Save & Test Connection';
      return;
    }

    const result = await API.testConnection(url);
    if (result.ok) {
      APP_CONFIG.setBackendUrl(url);
      closeConfigModal();
      TOAST.show('Connected to backend!', 'success');
      updateConnectionBanner();
    } else {
      TOAST.show(`Connection failed: ${result.msg}`, 'error');
    }
    saveConfigBtn.disabled = false;
    saveConfigBtn.innerHTML = '<i class="fas fa-save"></i> Save & Test Connection';
  });

  // ── Banner visibility ─────────────────────────────────────────
  // Uses a SHORT timeout (6 s) — just a quick optimistic check.
  // If the backend is cold-starting on Railway we don't want to
  // show a scary "unreachable" banner for 50 seconds; real errors
  // will surface naturally when the user sends a message.
  //
  // Phase 1 customer-facing cleanup: all technical wording removed.
  // Customers only ever see the friendly FRIENDLY_CONNECTION_MSG text
  // and a "Request Help" button (opens the existing lead form) —
  // never "demo mode", "backend", or a URL.
  function updateConnectionBanner() {
    if (!connBanner) return;

    // Demo mode (no backend URL configured at all) — still friendly wording only.
    if (APP_CONFIG.isDemoMode()) {
      connBanner.classList.remove('hidden');
      if (connMsg) connMsg.textContent = FRIENDLY_CONNECTION_MSG;
      return;
    }

    // Optimistic: hide banner immediately, only show if genuinely unreachable
    connBanner.classList.add('hidden');

    API.testConnection(APP_CONFIG.getBackendUrl(), 6000).then(res => {
      if (res.ok) {
        connBanner.classList.add('hidden');
      } else {
        // Only show the banner for hard failures (not timeouts / cold-starts)
        const msg = (res.msg || '').toLowerCase();
        const isColdStart = msg.includes('timeout') || msg.includes('starting');
        if (!isColdStart) {
          connBanner.classList.remove('hidden');
          if (connMsg) connMsg.textContent = FRIENDLY_CONNECTION_MSG;
        }
        // If it's just a cold-start timeout, stay hidden — Tori will work once warm
      }
    });
  }

  updateConnectionBanner();

  // ── "Request Help" button (replaces old "Configure" banner button) ──
  // Uses the EXISTING lead-capture system (js/leads.js) — no new form
  // was built. Falls back gracefully if LEADS or the chat container
  // isn't available for any reason.
  requestHelpBtn?.addEventListener('click', () => {
    const container = document.getElementById('chat-messages');
    if (window.LEADS && container && typeof LEADS.showLeadForm === 'function') {
      LEADS.showLeadForm({ trigger: 'handover', label: 'Consultant recommended', message: '' }, container);
      container.scrollTop = container.scrollHeight;
    } else {
      TOAST?.show('Please contact our team directly for assistance.', 'info');
    }
    connBanner?.classList.add('hidden');
  });

  // ── Keyboard shortcuts ────────────────────────────────────────
  document.addEventListener('keydown', e => {
    // Esc → close any open modal
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay:not(.hidden)').forEach(m => m.classList.add('hidden'));
    }
    // Ctrl/Cmd + K → focus chat input
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      document.getElementById('chat-input')?.focus();
    }
  });

  // ── Update business name if stored ───────────────────────────
  const businessName = APP_CONFIG.getBusinessName();
  document.querySelectorAll('.brand-name').forEach(el => {
    el.textContent = businessName;
  });
  document.title = `${businessName} – AI Assistant`;

  // ── Service Worker (optional PWA support) ────────────────────
  if ('serviceWorker' in navigator) {
    try {
      await navigator.serviceWorker.register('sw.js');
    } catch {
      // No service worker — fine for non-PWA deployments
    }
  }

})();
