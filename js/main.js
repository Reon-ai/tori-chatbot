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
  const configModal     = document.getElementById('config-modal');
  const backendUrlInput = document.getElementById('backend-url-input');
  const saveConfigBtn   = document.getElementById('save-config');
  const cancelConfigBtn = document.getElementById('cancel-config');
  const closeConfigBtn  = document.getElementById('close-config-modal');
  const configureBtn    = document.getElementById('configure-backend-btn');
  const connBanner      = document.getElementById('connection-banner');
  const connMsg         = document.getElementById('connection-msg');

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

  configureBtn?.addEventListener('click', openConfigModal);
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
  function updateConnectionBanner() {
    if (!connBanner) return;
    if (APP_CONFIG.isDemoMode()) {
      connBanner.classList.remove('hidden');
      if (connMsg) connMsg.textContent = '⚡ Running in demo mode — configure backend to enable full RAG pipeline';
    } else {
      // Check if backend is alive
      API.testConnection(APP_CONFIG.getBackendUrl()).then(res => {
        if (res.ok) {
          connBanner.classList.add('hidden');
        } else {
          connBanner.classList.remove('hidden');
          if (connMsg) connMsg.textContent = `Backend unreachable: ${res.msg}`;
        }
      });
    }
  }

  updateConnectionBanner();

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
