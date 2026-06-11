/**
 * theme.js — Dark/light mode toggle with persistence
 */

'use strict';

const THEME = (() => {
  const DARK  = 'dark-mode';
  const LIGHT = 'light-mode';

  function getCurrent() {
    return APP_CONFIG.get(APP_CONFIG.KEYS.THEME, 'light');
  }

  function apply(mode) {
    document.body.classList.remove(DARK, LIGHT);
    document.body.classList.add(mode === 'dark' ? DARK : LIGHT);

    // Update all theme toggle buttons on page
    document.querySelectorAll('#theme-toggle, #theme-toggle-admin').forEach(btn => {
      if (!btn) return;
      const icon = btn.querySelector('i');
      if (!icon) return;
      icon.className = mode === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
      btn.title = mode === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
    });
  }

  function toggle() {
    const current = getCurrent();
    const next    = current === 'dark' ? 'light' : 'dark';
    APP_CONFIG.set(APP_CONFIG.KEYS.THEME, next);
    apply(next);
  }

  function init() {
    // Apply saved preference (or system preference)
    let saved = getCurrent();
    if (!APP_CONFIG.get(APP_CONFIG.KEYS.THEME)) {
      const prefersDark = window.matchMedia?.('(prefers-color-scheme: dark)').matches;
      saved = prefersDark ? 'dark' : 'light';
    }
    apply(saved);

    // Bind buttons
    document.querySelectorAll('#theme-toggle, #theme-toggle-admin').forEach(btn => {
      btn?.addEventListener('click', toggle);
    });

    // Respond to system changes (only if user hasn't set a preference)
    window.matchMedia?.('(prefers-color-scheme: dark)').addEventListener('change', e => {
      if (!APP_CONFIG.get(APP_CONFIG.KEYS.THEME)) apply(e.matches ? 'dark' : 'light');
    });
  }

  return { init, toggle, apply, getCurrent };
})();

window.THEME = THEME;


/**
 * toast.js — lightweight notification toasts
 */
const TOAST = (() => {
  const ICONS = {
    success: '<i class="fas fa-check-circle" style="color:var(--success)"></i>',
    error:   '<i class="fas fa-times-circle" style="color:var(--danger)"></i>',
    warning: '<i class="fas fa-exclamation-triangle" style="color:var(--warning)"></i>',
    info:    '<i class="fas fa-info-circle" style="color:var(--info)"></i>',
  };

  function show(message, type = 'info', duration = 3500) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
      <span class="toast-icon">${ICONS[type] || ICONS.info}</span>
      <span class="toast-text">${message}</span>
    `;
    container.appendChild(toast);

    const remove = () => {
      toast.classList.add('removing');
      toast.addEventListener('animationend', () => toast.remove(), { once: true });
    };

    setTimeout(remove, duration);
    toast.addEventListener('click', remove);
  }

  return { show };
})();

window.TOAST = TOAST;
