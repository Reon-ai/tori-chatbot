/**
 * chat.js — All chat UI logic: messages, typing, input, suggestions
 */

'use strict';

const CHAT = (() => {
  // ── State ─────────────────────────────────────────────────────
  let sessionId  = '';
  let isWaiting  = false;
  let abortCtrl  = null;
  let messageIdx = 0;

  // ── DOM refs ──────────────────────────────────────────────────
  const refs = {};

  function initRefs() {
    refs.messagesContainer = document.getElementById('chat-messages');
    refs.form              = document.getElementById('chat-form');
    refs.input             = document.getElementById('chat-input');
    refs.sendBtn           = document.getElementById('send-btn');
    refs.typingIndicator   = document.getElementById('typing-indicator');
    refs.suggestionsRow    = document.getElementById('suggestions-row');
    refs.statusDot         = document.getElementById('status-dot');
    refs.statusLabel       = document.getElementById('status-label');
    refs.sessionDisplay    = document.getElementById('session-display');
    refs.charCount         = document.getElementById('char-count');
    refs.clearBtn          = document.getElementById('clear-chat-btn');
    refs.clearModal        = document.getElementById('clear-modal');
    refs.confirmClear      = document.getElementById('confirm-clear');
    refs.cancelClear       = document.getElementById('cancel-clear');
    refs.closeClearModal   = document.getElementById('close-clear-modal');
  }

  // ── Session init ──────────────────────────────────────────────
  function initSession() {
    sessionId = APP_CONFIG.getOrCreateSession();
    if (refs.sessionDisplay) {
      refs.sessionDisplay.textContent = `Session: ${sessionId.split('-')[0]}`;
    }
  }

  // ── Welcome message ───────────────────────────────────────────
  function showWelcome() {
    const businessName = APP_CONFIG.getBusinessName();
    const div = document.createElement('div');
    div.className = 'welcome-message';
    div.innerHTML = `
      <div class="welcome-icon">
        <div class="tori-welcome-tile">
          <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" class="tori-tile-svg" aria-hidden="true">
            <rect class="tile-rect-outer" x="4" y="4" width="56" height="56" rx="12"/>
            <rect class="tile-rect-inner" x="16" y="16" width="32" height="32" rx="6"/>
            <rect class="tile-dot" x="27" y="27" width="10" height="10" rx="2"/>
          </svg>
        </div>
      </div>
      <h2>Welcome to ${escapeHtml(businessName)}</h2>
      <p>I'm your AI assistant. Ask me anything about products, orders, shipping, returns, or policies!</p>
    `;
    refs.messagesContainer.appendChild(div);
  }

  // ── Escape HTML ───────────────────────────────────────────────
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // ── Format bot markdown-lite ──────────────────────────────────
  function formatMessage(text) {
    if (!text) return '';
    let html = escapeHtml(text);
    // Bold: **text**
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    // Italic: *text*
    html = html.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g, '<em>$1</em>');
    // Unordered lists
    html = html.replace(/^[\s]*[-*•]\s+(.+)$/gm, '<li>$1</li>');
    html = html.replace(/((?:<li>.*<\/li>\n?)+)/g, '<ul>$1</ul>');
    // Ordered lists
    html = html.replace(/^\d+\.\s+(.+)$/gm, '<li>$1</li>');
    // Line breaks → paragraphs
    html = html.split(/\n{2,}/).map(p => p.trim() ? `<p>${p.replace(/\n/g, '<br/>')}</p>` : '').join('');
    // If no <p> tags yet, wrap
    if (!html.includes('<p>') && !html.includes('<ul>') && !html.includes('<li>')) {
      html = `<p>${html}</p>`;
    }
    return html;
  }

  // ── Timestamp helper ──────────────────────────────────────────
  function formatTime(date = new Date()) {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

  // ── Add message to UI ─────────────────────────────────────────
  function addMessage(role, text, options = {}) {
    const { timestamp = new Date(), messageId = null } = options;
    const idx = ++messageIdx;

    // Hide suggestions on first real message
    if (refs.suggestionsRow && idx >= 1) {
      refs.suggestionsRow.style.display = 'none';
    }

    const row  = document.createElement('div');
    const isBot = role === 'bot';
    row.className = `msg-row ${isBot ? 'bot' : 'user'}`;
    row.dataset.msgIndex = idx;
    if (messageId) row.dataset.messageId = messageId;

    const avatarEmoji = isBot ? '🤖' : '👤';
    const bubbleContent = isBot ? formatMessage(text) : `<p>${escapeHtml(text)}</p>`;

    // Build rating buttons (only for bot)
    const ratingHtml = isBot ? `
      <button class="rating-btn up" aria-label="Helpful" title="Helpful">
        <i class="fas fa-thumbs-up"></i>
      </button>
      <button class="rating-btn down" aria-label="Not helpful" title="Not helpful">
        <i class="fas fa-thumbs-down"></i>
      </button>` : '';

    row.innerHTML = `
      <div class="msg-avatar" aria-hidden="true">${avatarEmoji}</div>
      <div class="msg-body">
        <div class="msg-bubble">${bubbleContent}</div>
        <div class="msg-meta">
          <span class="msg-time">${formatTime(timestamp)}</span>
          <button class="msg-action-btn copy-btn" title="Copy message" aria-label="Copy message">
            <i class="fas fa-copy"></i>
          </button>
          ${ratingHtml}
        </div>
      </div>
    `;

    // Copy button handler
    row.querySelector('.copy-btn').addEventListener('click', () => {
      navigator.clipboard?.writeText(text).then(() => {
        TOAST.show('Copied to clipboard', 'success');
      }).catch(() => {
        TOAST.show('Copy failed', 'error');
      });
    });

    // Rating button handlers
    if (isBot) {
      const upBtn   = row.querySelector('.rating-btn.up');
      const downBtn = row.querySelector('.rating-btn.down');

      const ratingHandler = async (btn, ratingValue) => {
        if (btn.classList.contains('active')) return;
        upBtn.classList.remove('active');
        downBtn.classList.remove('active');
        btn.classList.add('active');
        TOAST.show(ratingValue === 1 ? 'Thanks for the feedback! 👍' : 'Thanks! We\'ll improve. 👎', 'info');
        if (messageId) {
          try { await API.submitRating(messageId, ratingValue); } catch {}
        }
        // Save rating to demo storage
        saveRatingToDemo(messageId, ratingValue);
      };

      upBtn.addEventListener('click',   () => ratingHandler(upBtn, 1));
      downBtn.addEventListener('click', () => ratingHandler(downBtn, -1));
    }

    refs.messagesContainer.appendChild(row);
    scrollToBottom();
    return row;
  }

  function saveRatingToDemo(messageId, rating) {
    const convs = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, []);
    const conv = convs.find(c => c.id === messageId);
    if (conv) {
      conv.rating = rating;
      APP_CONFIG.set(APP_CONFIG.KEYS.CONVERSATIONS, convs);
    }
  }

  // ── Error bubble ──────────────────────────────────────────────
  function addErrorMessage(text) {
    const row = document.createElement('div');
    row.className = 'msg-row bot';
    row.innerHTML = `
      <div class="msg-avatar" aria-hidden="true">⚠️</div>
      <div class="msg-body">
        <div class="msg-bubble" style="border-color: var(--danger); color: var(--danger);">
          <p><strong>Something went wrong:</strong> ${escapeHtml(text)}</p>
          <p style="margin-top:.5rem; font-size:.82rem; opacity:.8;">Please try again or check your connection.</p>
        </div>
        <div class="msg-meta"><span class="msg-time">${formatTime()}</span></div>
      </div>
    `;
    refs.messagesContainer.appendChild(row);
    scrollToBottom();
  }

  // ── Typing indicator ──────────────────────────────────────────
  function showTyping() {
    refs.typingIndicator?.classList.remove('hidden');
    scrollToBottom();
  }
  function hideTyping() {
    refs.typingIndicator?.classList.add('hidden');
  }

  // ── Scroll ────────────────────────────────────────────────────
  function scrollToBottom() {
    requestAnimationFrame(() => {
      refs.messagesContainer.scrollTop = refs.messagesContainer.scrollHeight;
    });
  }

  // ── Status indicator ──────────────────────────────────────────
  function setStatus(state, label) {
    if (!refs.statusDot || !refs.statusLabel) return;
    refs.statusDot.className = `status-dot ${state}`;
    refs.statusLabel.textContent = label;
  }

  // ── Disable / enable input ────────────────────────────────────
  function setInputEnabled(enabled) {
    isWaiting = !enabled;
    if (refs.input)   refs.input.disabled = !enabled;
    if (refs.sendBtn) refs.sendBtn.disabled = !enabled;
  }

  // ── Send message ──────────────────────────────────────────────
  async function sendMessage(text) {
    const msg = text.trim();
    if (!msg || isWaiting) return;

    setInputEnabled(false);
    setStatus('busy', 'Thinking…');
    showTyping();

    addMessage('user', msg);

    if (refs.input) { refs.input.value = ''; autoResize(); }
    if (refs.charCount) refs.charCount.textContent = '0/1000';

    abortCtrl = new AbortController();
    const startTime = Date.now();

    try {
      const data = await API.chat(msg, sessionId, abortCtrl.signal);
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

      hideTyping();
      if (data?.response) {
        addMessage('bot', data.response, { messageId: data.message_id });
      } else {
        addErrorMessage('Empty response received');
      }

      setStatus('online', `Ready · ${elapsed}s`);
    } catch (err) {
      hideTyping();
      if (err.name === 'AbortError') {
        setStatus('online', 'Cancelled');
      } else {
        setStatus('offline', 'Error');
        addErrorMessage(err.message || 'Request failed');
      }
    } finally {
      setInputEnabled(true);
      abortCtrl = null;
      setTimeout(() => setStatus('online', 'Assistant Ready'), 3000);
    }
  }

  // ── Auto-resize textarea ──────────────────────────────────────
  function autoResize() {
    if (!refs.input) return;
    refs.input.style.height = 'auto';
    refs.input.style.height = Math.min(refs.input.scrollHeight, 160) + 'px';
  }

  // ── Clear chat ────────────────────────────────────────────────
  function clearChat() {
    refs.messagesContainer.innerHTML = '';
    messageIdx = 0;
    sessionId = APP_CONFIG.refreshSession();
    if (refs.sessionDisplay) refs.sessionDisplay.textContent = `Session: ${sessionId.split('-')[0]}`;
    if (refs.suggestionsRow) refs.suggestionsRow.style.display = '';
    showWelcome();
    TOAST.show('Conversation cleared', 'success');
  }

  // ── Event bindings ─────────────────────────────────────────────
  function bindEvents() {
    // Form submit
    refs.form?.addEventListener('submit', e => {
      e.preventDefault();
      sendMessage(refs.input?.value || '');
    });

    // Enter key (Shift+Enter = newline)
    refs.input?.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage(refs.input.value || '');
      }
    });

    // Auto-resize & char count
    refs.input?.addEventListener('input', () => {
      autoResize();
      const len = (refs.input.value || '').length;
      if (refs.charCount) {
        refs.charCount.textContent = `${len}/1000`;
        refs.charCount.style.color = len > 900 ? 'var(--danger)' : '';
      }
    });

    // Suggestion chips
    document.querySelectorAll('.suggestion-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        sendMessage(chip.dataset.q || chip.textContent.trim());
      });
    });

    // Clear chat button
    refs.clearBtn?.addEventListener('click', () => {
      refs.clearModal?.classList.remove('hidden');
    });
    refs.cancelClear?.addEventListener('click', () => refs.clearModal?.classList.add('hidden'));
    refs.closeClearModal?.addEventListener('click', () => refs.clearModal?.classList.add('hidden'));
    refs.confirmClear?.addEventListener('click', () => {
      refs.clearModal?.classList.add('hidden');
      clearChat();
    });

    // Close modal on backdrop click
    refs.clearModal?.addEventListener('click', e => {
      if (e.target === refs.clearModal) refs.clearModal.classList.add('hidden');
    });
  }

  // ── Public init ───────────────────────────────────────────────
  function init() {
    initRefs();
    initSession();
    showWelcome();
    bindEvents();
    autoResize();
    refs.input?.focus();
  }

  return { init, addMessage, addErrorMessage, clearChat, setStatus };
})();

window.CHAT = CHAT;
