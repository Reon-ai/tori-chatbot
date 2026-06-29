/**
 * chat.js — All chat UI logic: messages, typing, voice input, lead capture
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
    refs.micBtn            = document.getElementById('mic-btn');
    refs.micIcon           = document.getElementById('mic-icon');
    refs.listeningBar      = document.getElementById('voice-listening-bar');
    refs.voiceCancelBtn    = document.getElementById('voice-cancel-btn');
    refs.typingIndicator   = document.getElementById('typing-indicator');
    
    refs.statusDot         = document.getElementById('status-dot');
    refs.statusLabel       = document.getElementById('status-label');
    refs.clearBtn          = document.getElementById('clear-chat-btn');
    refs.clearModal        = document.getElementById('clear-modal');
    refs.confirmClear      = document.getElementById('confirm-clear');
    refs.cancelClear       = document.getElementById('cancel-clear');
    refs.closeClearModal   = document.getElementById('close-clear-modal');
  }

  // ── Voice Recognition ─────────────────────────────────────────
  const VOICE = (() => {
    let isListening = false;
    let initialised = false;

    function getSpeechAPI() {
      return window.SpeechRecognition ||
             window.webkitSpeechRecognition ||
             null;
    }

    // ── MediaRecorder-based recording (no cloud dependency) ──────
    // Instead of Web Speech API cloud transcription (which is blocked on
    // gensparkspace.com by Edge/Chrome's speech servers), we:
    // 1. Record audio with MediaRecorder (pure browser, no cloud)
    // 2. Send the audio blob to Railway backend → OpenAI Whisper
    // 3. Get transcript back and fill the input

    let mediaRecorder  = null;
    let audioChunks    = [];
    let recordingStream = null;

    async function startListening(refs) {
      if (isListening) return;
      try {
        recordingStream = await navigator.mediaDevices.getUserMedia({ audio: true });
        audioChunks  = [];

        // Pick best supported format
        const mimeType = MediaRecorder.isTypeSupported('audio/webm;codecs=opus')
          ? 'audio/webm;codecs=opus'
          : MediaRecorder.isTypeSupported('audio/webm')
          ? 'audio/webm'
          : 'audio/ogg';

        mediaRecorder = new MediaRecorder(recordingStream, { mimeType });

        mediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) audioChunks.push(e.data);
        };

        mediaRecorder.onstop = async () => {
          // Stop all mic tracks to release the mic indicator
          recordingStream?.getTracks().forEach(t => t.stop());
          recordingStream = null;

          const blob = new Blob(audioChunks, { type: mimeType });
          audioChunks = [];

          if (blob.size < 1000) {
            // Too small — no speech captured
            stopListening(refs);
            return;
          }

          // Show transcribing state
          refs.listeningBar?.classList.remove('hidden');
          const textEl = refs.listeningBar?.querySelector('.voice-listening-text');
          if (textEl) textEl.textContent = 'Transcribing…';

          try {
            const transcript = await transcribeAudio(blob, mimeType);
            stopListening(refs);
            if (transcript && transcript.trim()) {
              refs.input.value = transcript.trim();
              autoResize();
              setTimeout(() => {
                refs.form?.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
              }, 300);
            }
          } catch (err) {
            stopListening(refs);
            TOAST?.show(`Transcription failed: ${err.message}`, 'warning');
          }
        };

        mediaRecorder.start(250); // collect chunks every 250ms
        isListening = true;
        refs.micBtn?.classList.add('listening');
        refs.listeningBar?.classList.remove('hidden');
        const textEl = refs.listeningBar?.querySelector('.voice-listening-text');
        if (textEl) textEl.textContent = 'Listening… speak now';
        refs.input.placeholder = 'Listening…';

      } catch (err) {
        isListening = false;
        if (err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError') {
          TOAST?.show('Microphone access denied — click the 🔒 padlock and set Microphone to Allow.', 'warning');
        } else if (err.name === 'NotFoundError') {
          TOAST?.show('No microphone found. Please connect a microphone.', 'warning');
        } else {
          TOAST?.show(`Microphone error: ${err.message}`, 'warning');
        }
      }
    }

    function stopListening(refs) {
      isListening = false;
      if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
      }
      recordingStream?.getTracks().forEach(t => t.stop());
      recordingStream = null;
      refs.micBtn?.classList.remove('listening');
      refs.listeningBar?.classList.add('hidden');
      const textEl = refs.listeningBar?.querySelector('.voice-listening-text');
      if (textEl) textEl.textContent = 'Listening… speak now';
      refs.input.placeholder = 'Ask Tori anything…';
    }

    async function transcribeAudio(blob, mimeType) {
      const base = APP_CONFIG.getBackendUrl();
      // Extension hint for Whisper
      const ext  = mimeType.includes('ogg') ? 'ogg' : 'webm';
      const fd   = new FormData();
      fd.append('file', blob, `audio.${ext}`);

      const resp = await fetch(`${base}/api/chat/transcribe`, {
        method: 'POST',
        body:   fd,
        signal: AbortSignal.timeout(20000),
      });

      if (!resp.ok) {
        const j = await resp.json().catch(() => ({}));
        throw new Error(j.detail || `HTTP ${resp.status}`);
      }
      const data = await resp.json();
      return data.transcript || data.text || '';
    }

    function init(refs) {
      // MediaRecorder is supported in all modern browsers — no feature check needed
      if (initialised) { refs.micBtn?.classList.remove('hidden'); return; }

      // Check mic API available
      if (!navigator.mediaDevices?.getUserMedia) return;
      initialised = true;
      refs.micBtn?.classList.remove('hidden');

      // ── Mic button: tap to start, tap again to stop ────────────
      refs.micBtn?.addEventListener('click', () => {
        if (isListening) {
          // User tapped to stop — commit what was recorded
          if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            mediaRecorder.stop();   // triggers onstop → transcribe
          }
          refs.micBtn?.classList.remove('listening');
        } else {
          startListening(refs);
        }
      });

      // ── Cancel button — abort without sending ─────────────────
      refs.voiceCancelBtn?.addEventListener('click', () => {
        audioChunks = [];  // discard recorded audio
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
          mediaRecorder.onstop = () => {
            recordingStream?.getTracks().forEach(t => t.stop());
            recordingStream = null;
          };
          mediaRecorder.stop();
        }
        stopListening(refs);
        refs.input.value = '';
        autoResize();
      });
    }

    return { init };
  })();

  // ── Session init ──────────────────────────────────────────────
  function initSession() {
    sessionId = APP_CONFIG.getOrCreateSession();
    // Notify the form renderer of the current session
    FORMS?.setSession(sessionId);
  }

  // ── Welcome message ───────────────────────────────────────────
  function showWelcome() {
    const div = document.createElement('div');
    div.className = 'welcome-message';
    div.innerHTML = `
      <div class="welcome-icon">
        <div class="tori-welcome-tile">
          <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" class="tori-tile-svg" aria-hidden="true">
            <rect class="tile-rect-outer" x="8" y="8" width="48" height="48" rx="0"/>
            <rect class="tile-rect-inner" x="20" y="20" width="24" height="24" rx="0"/>
          </svg>
        </div>
      </div>
      <h2>Hi, I'm <em>Tori</em></h2>
      <p>Your Tiletoria flooring, tile and design concierge.<br>Ask me anything — I'm here to help you make the right choice.</p>
      <div class="welcome-caps">
        <button class="welcome-cap-btn" data-q="What tiles do you have in stock?">
          <svg viewBox="0 0 20 20" width="14" height="14"><rect x="1" y="1" width="8" height="8" fill="#FCE300"/><rect x="11" y="1" width="8" height="8" fill="#FCE300"/><rect x="1" y="11" width="8" height="8" fill="#FCE300"/><rect x="11" y="11" width="8" height="8" fill="#FCE300"/></svg>
          Tiles
        </button>
        <button class="welcome-cap-btn" data-q="Tell me about your sanware range">
          <i class="fas fa-shower"></i>
          Sanware
        </button>
        <button class="welcome-cap-btn" data-q="What vinyl and laminate flooring options do you offer?">
          <i class="fas fa-layer-group"></i>
          Vinyl &amp; Laminate
        </button>
        <button class="welcome-cap-btn" data-q="What are your store locations?">
          <i class="fas fa-location-dot"></i>
          Store Locations
        </button>
      </div>
    `;
    refs.messagesContainer.appendChild(div);

    // Make welcome cap buttons clickable — send question on click
    div.querySelectorAll('.welcome-cap-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const q = btn.dataset.q;
        if (q && refs.input) {
          refs.input.value = q;
          refs.input.dispatchEvent(new Event('input'));
          refs.form.dispatchEvent(new Event('submit', { bubbles: true, cancelable: true }));
        }
      });
    });
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

    const row  = document.createElement('div');
    const isBot = role === 'bot';
    row.className = `msg-row ${isBot ? 'bot' : 'user'}`;
    row.dataset.msgIndex = idx;
    if (messageId) row.dataset.messageId = messageId;

    const bubbleContent = isBot ? formatMessage(text) : `<p>${escapeHtml(text)}</p>`;

    // Bot avatar = tiny yellow tile square; User avatar = person icon
    const avatarHtml = isBot
      ? `<div class="bot-avatar-tile"></div>`
      : `<i class="fas fa-user user-avatar-icon"></i>`;

    // Build rating buttons (only for bot)
    const ratingHtml = isBot ? `
      <button class="rating-btn up" aria-label="Helpful" title="Helpful">
        <i class="fas fa-thumbs-up"></i>
      </button>
      <button class="rating-btn down" aria-label="Not helpful" title="Not helpful">
        <i class="fas fa-thumbs-down"></i>
      </button>` : '';

    row.innerHTML = `
      <div class="msg-avatar" aria-hidden="true">${avatarHtml}</div>
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

  // ── Frontend intent fallback ─────────────────────────────────
  // Used ONLY when the backend hasn't redeployed yet.
  // Maps user message → formId matching /forms/<formId>_form.json
  const _FRONTEND_FALLBACK = [
    [/\bquotes?\b|\bquotation\b|\bkwotasie\b|\bhow\s+much\b|\bwat\s+kos\b|\bhoeveel\b|\bpryse?\b|\bi\s+want\s+to\s+(buy|order)\b|\bready\s+to\s+(buy|order)\b/i, 'tile_quote', 'I can help with that. Please complete the quick form below and a consultant will be in touch.'],
    [/\b(call|phone|ring)\s+me\b|\bcontact\s+me\b|\bget\s+back\s+to\s+me\b|\bwhatsapp\s+me\b|\bspeak\s+to\s+(a\s+)?(person|consultant)\b|\bkan\s+iemand\b/i, 'contact_me', 'Sure — leave your details below and a consultant will call or WhatsApp you.'],
    [/\bcontractor\b|\bbuilder\b|\btrade\s*(price|account)?\b|\bbulk\s*(order|buy)?\b|\barchitect\b|\binterior\s+design\w*\b/i, 'contractor_quote', 'Great — we love working with trade professionals. Please complete the form below.'],
    [/\bbook\s+an?\s+appointment\b|\bvisit\s+the\s+showroom\b|\bshowroom\s+appointment\b/i, 'store_assistance', 'We would love to see you! Please complete the booking form below.'],
    [/\bwhich\s+(tile|product)\b|\bhelp\s+me\s+choose\b|\brecommend\s+(a\s+)?(tile|product)\b/i, 'product_enquiry', 'Happy to help you find the right product. Please share a few details below.'],
    [/\bsample\b|\bsee\s+the\s+tile\b/i, 'sample_request', 'Seeing is believing! Fill in the form and we will arrange samples for you.'],
    [/\bin\s+stock\b|\bdo\s+you\s+(have|stock)\b|\bavailab\w+\b/i, 'product_enquiry', 'Let me check that for you. Please complete the short form below.'],
    [/\bdeliver\w*\b|\bshipping\b|\bdo\s+you\s+deliver\b/i, 'contact_me', 'We can arrange delivery. Leave your details below and we will confirm costs.'],
  ];

  function _frontendFallbackAction(userMessage) {
    for (const [re, formId, message] of _FRONTEND_FALLBACK) {
      if (re.test(userMessage)) return { formId, message };
    }
    return null;
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
    abortCtrl = new AbortController();
    const startTime = Date.now();

    try {
      const data = await API.chat(msg, sessionId, abortCtrl.signal);
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);

      hideTyping();
      if (data?.response) {
        // ── Clean any legacy [CONSULTANT_NEEDED] markers ──────────
        const cleanResponse = data.response.replaceAll('[CONSULTANT_NEEDED]', '').trim();

        addMessage('bot', cleanResponse, { messageId: data.message_id });

        // ── Structured form action ────────────────────────────────
        // PRIMARY:  backend returns data.form_action = {formId, message}
        // FALLBACK: frontend regex detects intent if backend not yet redeployed
        const action = data.form_action || _frontendFallbackAction(msg);
        if (action?.formId) {
          console.log('[CHAT] Form action:', action.formId, '— rendering form');
          FORMS?.renderForm(action.formId, action.message, refs.messagesContainer, sessionId);
        }

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
      setTimeout(() => setStatus('online', 'Tori · Ready'), 3000);
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
    FORMS?.setSession(sessionId);
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
    // Try immediately, then retry after 800ms (some browsers need page to fully settle)
    VOICE.init(refs);
    setTimeout(() => VOICE.init(refs), 800);
    refs.input?.focus();
  }

  return { init, addMessage, addErrorMessage, clearChat, setStatus };
})();

window.CHAT = CHAT;

