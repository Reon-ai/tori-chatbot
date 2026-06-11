/**
 * config.js — Global application configuration & constants
 * Loaded first on every page; sets up APP_CONFIG used by all modules.
 */

'use strict';

const APP_CONFIG = (() => {
  // ── Storage keys ────────────────────────────────────────────
  const STORAGE_KEYS = {
    BACKEND_URL:   'rag_backend_url',
    SESSION_ID:    'rag_session_id',
    THEME:         'rag_theme',
    ADMIN_AUTH:    'rag_admin_auth',
    RAG_SETTINGS:  'rag_settings',
    BUSINESS_NAME: 'rag_business_name',
    CONVERSATIONS: 'rag_demo_conversations',
    DOCUMENTS:     'rag_demo_documents',
    ANALYTICS:     'rag_demo_analytics',
  };

  // ── Defaults ─────────────────────────────────────────────────
  const DEFAULTS = {
    BACKEND_URL:   '',                  // empty = demo mode
    BUSINESS_NAME: 'Tori',
    ADMIN_PASSWORD: 'admin123',         // stored hashed in production
    RAG: {
      chunkSize:      800,
      chunkOverlap:   150,
      topK:           5,
      similarity:     0.7,
      model:          'gpt-4o-mini',
      temperature:    0.3,
      maxTokens:      500,
      memoryTurns:    5,
    },
  };

  // ── Helpers ──────────────────────────────────────────────────
  function get(key, fallback = null) {
    try {
      const raw = localStorage.getItem(key);
      if (raw === null) return fallback;
      return JSON.parse(raw);
    } catch {
      return fallback;
    }
  }

  function set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; }
    catch (e) { console.warn('[Config] localStorage write failed:', e); return false; }
  }

  function remove(key) {
    try { localStorage.removeItem(key); } catch {}
  }

  // ── Session ID (UUID v4-ish) ─────────────────────────────────
  function generateSessionId() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
      const r = Math.random() * 16 | 0;
      return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
  }

  function getOrCreateSession() {
    let sid = get(STORAGE_KEYS.SESSION_ID);
    if (!sid) {
      sid = generateSessionId();
      set(STORAGE_KEYS.SESSION_ID, sid);
    }
    return sid;
  }

  function refreshSession() {
    const sid = generateSessionId();
    set(STORAGE_KEYS.SESSION_ID, sid);
    return sid;
  }

  // ── Simple hash for admin password ──────────────────────────
  async function hashString(str) {
    if (!crypto?.subtle) {
      // Fallback: very basic checksum (not secure – use server auth in production)
      let h = 0;
      for (let i = 0; i < str.length; i++) h = (Math.imul(31, h) + str.charCodeAt(i)) | 0;
      return h.toString(16);
    }
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2,'0')).join('');
  }

  // ── API helpers ──────────────────────────────────────────────
  function getBackendUrl() {
    return (get(STORAGE_KEYS.BACKEND_URL, '') || '').replace(/\/$/, '');
  }
  function setBackendUrl(url) { set(STORAGE_KEYS.BACKEND_URL, (url || '').trim()); }
  function isDemoMode() { return !getBackendUrl(); }

  // ── Settings helpers ─────────────────────────────────────────
  function getRagSettings() {
    return { ...DEFAULTS.RAG, ...(get(STORAGE_KEYS.RAG_SETTINGS, {})) };
  }
  function saveRagSettings(settings) { set(STORAGE_KEYS.RAG_SETTINGS, settings); }

  function getBusinessName() { return get(STORAGE_KEYS.BUSINESS_NAME, DEFAULTS.BUSINESS_NAME); }
  function setBusinessName(name) { set(STORAGE_KEYS.BUSINESS_NAME, name); }

  // ── Expose ────────────────────────────────────────────────────
  return {
    KEYS: STORAGE_KEYS,
    DEFAULTS,
    get, set, remove,
    generateSessionId,
    getOrCreateSession,
    refreshSession,
    hashString,
    getBackendUrl,
    setBackendUrl,
    isDemoMode,
    getRagSettings,
    saveRagSettings,
    getBusinessName,
    setBusinessName,
  };
})();

// Make available globally
window.APP_CONFIG = APP_CONFIG;
