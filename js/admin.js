/**
 * admin.js — Full admin panel logic:
 * authentication, tabs, documents, analytics, conversations, config
 */

'use strict';

(async function initAdmin() {

  THEME.init();

  // ══════════════════════════════════════════════════════════════
  // AUTH
  // ══════════════════════════════════════════════════════════════
  const loginOverlay = document.getElementById('admin-login-overlay');
  const adminApp     = document.getElementById('admin-app');
  const loginForm    = document.getElementById('admin-login-form');
  const passwordInput = document.getElementById('admin-password');
  const loginError   = document.getElementById('login-error');
  const togglePw     = document.getElementById('toggle-pw');
  const logoutBtn    = document.getElementById('admin-logout');

  const SESSION_KEY = 'rag_admin_session';

  function isAuthenticated() {
    return sessionStorage.getItem(SESSION_KEY) === 'true';
  }

  function showAdminApp() {
    loginOverlay?.classList.add('hidden');
    adminApp?.classList.remove('hidden');
  }

  function showLogin() {
    loginOverlay?.classList.remove('hidden');
    adminApp?.classList.add('hidden');
    sessionStorage.removeItem(SESSION_KEY);
  }

  if (isAuthenticated()) {
    showAdminApp();
    bootAdmin();
  } else {
    loginOverlay?.classList.remove('hidden');
  }

  loginForm?.addEventListener('submit', async e => {
    e.preventDefault();
    const pw = passwordInput?.value || '';
    if (!pw) return;

    loginError?.classList.add('hidden');
    const submitBtn = loginForm.querySelector('button[type="submit"]');
    if (submitBtn) { submitBtn.disabled = true; submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Verifying…'; }

    // Hash entered password and compare
    const enteredHash = await APP_CONFIG.hashString(pw);
    const storedPw    = APP_CONFIG.DEFAULTS.ADMIN_PASSWORD;
    const storedHash  = await APP_CONFIG.hashString(storedPw);

    // Also allow direct match for simplicity (plain text comparison fallback)
    const ok = enteredHash === storedHash || pw === storedPw;

    if (submitBtn) { submitBtn.disabled = false; submitBtn.innerHTML = '<i class="fas fa-sign-in-alt"></i> Sign In'; }

    if (ok) {
      sessionStorage.setItem(SESSION_KEY, 'true');
      showAdminApp();
      bootAdmin();
    } else {
      loginError?.classList.remove('hidden');
      passwordInput?.select();
    }
  });

  togglePw?.addEventListener('click', () => {
    const type = passwordInput?.type === 'password' ? 'text' : 'password';
    if (passwordInput) passwordInput.type = type;
    const icon = togglePw.querySelector('i');
    if (icon) icon.className = type === 'text' ? 'fas fa-eye-slash' : 'fas fa-eye';
  });

  logoutBtn?.addEventListener('click', () => {
    showLogin();
    TOAST.show('Signed out', 'info');
  });

  // ══════════════════════════════════════════════════════════════
  // BOOT (runs after auth)
  // ══════════════════════════════════════════════════════════════
  function bootAdmin() {
    initTabs();
    initSidebar();
    loadDashboard();
    initDocuments();
    initAnalytics();
    initConversations();
    initConfiguration();
  }

  // ══════════════════════════════════════════════════════════════
  // TABS
  // ══════════════════════════════════════════════════════════════
  function initTabs() {
    document.querySelectorAll('.nav-item').forEach(btn => {
      btn.addEventListener('click', () => {
        const tabId = btn.dataset.tab;
        // Activate button
        document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        // Show tab
        document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
        document.getElementById(`tab-${tabId}`)?.classList.add('active');
        // Lazy load
        if (tabId === 'analytics')     loadAnalytics();
        if (tabId === 'conversations') loadConversations();
        if (tabId === 'documents')     loadDocuments();
        // Close sidebar on mobile
        if (window.innerWidth < 768) closeSidebar();
      });
    });
  }

  // ══════════════════════════════════════════════════════════════
  // SIDEBAR (mobile)
  // ══════════════════════════════════════════════════════════════
  const sidebarEl     = document.getElementById('admin-sidebar');
  const sidebarToggle = document.getElementById('sidebar-toggle');

  function openSidebar()  { sidebarEl?.classList.add('open'); }
  function closeSidebar() { sidebarEl?.classList.remove('open'); }

  function initSidebar() {
    sidebarToggle?.addEventListener('click', () => {
      sidebarEl?.classList.contains('open') ? closeSidebar() : openSidebar();
    });
    document.addEventListener('click', e => {
      if (window.innerWidth < 768 &&
          sidebarEl?.classList.contains('open') &&
          !sidebarEl.contains(e.target) &&
          e.target !== sidebarToggle) {
        closeSidebar();
      }
    });
  }

  // ══════════════════════════════════════════════════════════════
  // DASHBOARD
  // ══════════════════════════════════════════════════════════════
  let dashboardCharts = {};

  async function loadDashboard() {
    // KPIs
    const convs = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, []);
    const docs   = APP_CONFIG.get(APP_CONFIG.KEYS.DOCUMENTS, []);
    const an     = APP_CONFIG.get(APP_CONFIG.KEYS.ANALYTICS, { queries: 0, totalTime: 0 });

    setKpi('kpi-total-queries', convs.length);
    setKpi('kpi-total-docs',    docs.length);
    setKpi('kpi-avg-response',  convs.length > 0 ? ((an.totalTime || 0) / convs.length / 1000).toFixed(1) : '—');
    setKpi('kpi-active-sessions', new Set(convs.slice(-50).map(c => c.session_id)).size);

    // Charts
    renderWeeklyQueriesChart(convs);
    renderQualityChart(convs);

    // System status
    await checkSystemStatus();
  }

  function setKpi(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  function renderWeeklyQueriesChart(convs) {
    const canvas = document.getElementById('chart-queries-week');
    if (!canvas) return;

    const days  = getLast7Days();
    const counts = days.map(day => convs.filter(c => c.timestamp?.startsWith(day)).length);

    if (dashboardCharts.weekly) dashboardCharts.weekly.destroy();
    dashboardCharts.weekly = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: days.map(d => new Date(d).toLocaleDateString([], { weekday: 'short', month: 'short', day: 'numeric' })),
        datasets: [{
          label: 'Queries',
          data: counts,
          backgroundColor: 'rgba(79,70,229,0.7)',
          borderColor: '#4F46E5',
          borderWidth: 2,
          borderRadius: 6,
        }],
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, ticks: { stepSize: 1, color: getComputedStyle(document.body).getPropertyValue('--text-3') } },
          x: { ticks: { color: getComputedStyle(document.body).getPropertyValue('--text-3') } },
        },
      },
    });
  }

  function renderQualityChart(convs) {
    const canvas = document.getElementById('chart-quality');
    if (!canvas) return;

    const positives = convs.filter(c => c.rating === 1).length;
    const negatives = convs.filter(c => c.rating === -1).length;
    const neutral   = convs.length - positives - negatives;

    if (dashboardCharts.quality) dashboardCharts.quality.destroy();
    dashboardCharts.quality = new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: ['Positive', 'Negative', 'No Rating'],
        datasets: [{
          data: [positives || 0, negatives || 0, neutral || 0],
          backgroundColor: ['#10B981', '#EF4444', '#E2E8F0'],
          borderWidth: 0,
        }],
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        cutout: '65%',
        plugins: { legend: { position: 'bottom', labels: { font: { size: 11 } } } },
      },
    });
  }

  async function checkSystemStatus() {
    const backendUrl = APP_CONFIG.getBackendUrl();

    function setBadge(id, text, cls) {
      const el = document.getElementById(id);
      if (!el) return;
      el.textContent = text;
      el.className = `status-badge ${cls}`;
    }

    if (!backendUrl) {
      setBadge('sys-backend', 'Demo Mode', 'checking');
      setBadge('sys-vectordb', 'Not Connected', 'offline');
      setBadge('sys-openai',   'Not Connected', 'offline');
      setBadge('sys-sqlite',   'Demo Mode', 'checking');
      return;
    }

    setBadge('sys-backend', 'Checking…', 'checking');
    const result = await API.testConnection(backendUrl);
    setBadge('sys-backend', result.ok ? 'Online' : 'Offline', result.ok ? 'online' : 'offline');

    if (result.ok) {
      try {
        const health = await API.GET('/health/detailed');
        setBadge('sys-vectordb', health.vectordb ? 'Online' : 'Offline', health.vectordb ? 'online' : 'offline');
        setBadge('sys-openai',   health.openai   ? 'Online' : 'Offline', health.openai   ? 'online' : 'offline');
        setBadge('sys-sqlite',   health.sqlite   ? 'Online' : 'Offline', health.sqlite   ? 'online' : 'offline');
      } catch {
        setBadge('sys-vectordb', 'Unknown', 'checking');
        setBadge('sys-openai',   'Unknown', 'checking');
        setBadge('sys-sqlite',   'Unknown', 'checking');
      }
    }
  }

  document.getElementById('refresh-status-btn')?.addEventListener('click', async () => {
    TOAST.show('Refreshing status…', 'info');
    await checkSystemStatus();
  });

  // ══════════════════════════════════════════════════════════════
  // DOCUMENTS
  // ══════════════════════════════════════════════════════════════
  const uploadZone     = document.getElementById('upload-zone');
  const fileInput      = document.getElementById('file-input');
  const browseFilesBtn = document.getElementById('browse-files-btn');
  const progressArea   = document.getElementById('upload-progress-area');
  const docsSearch     = document.getElementById('doc-search');
  const docsTbody      = document.getElementById('docs-tbody');
  const docCount       = document.getElementById('doc-count');
  const reindexBtn     = document.getElementById('reindex-btn');

  let allDocs = [];

  function initDocuments() {
    // Drag & drop
    uploadZone?.addEventListener('dragover', e => { e.preventDefault(); uploadZone.classList.add('drag-over'); });
    uploadZone?.addEventListener('dragleave', () => uploadZone.classList.remove('drag-over'));
    uploadZone?.addEventListener('drop', e => {
      e.preventDefault();
      uploadZone.classList.remove('drag-over');
      handleFiles([...e.dataTransfer.files]);
    });
    uploadZone?.addEventListener('click', e => {
      if (e.target !== browseFilesBtn) fileInput?.click();
    });
    browseFilesBtn?.addEventListener('click', e => { e.stopPropagation(); fileInput?.click(); });
    fileInput?.addEventListener('change', () => {
      if (fileInput.files.length) handleFiles([...fileInput.files]);
      fileInput.value = '';
    });

    // Search
    docsSearch?.addEventListener('input', () => renderDocsTable(docsSearch.value));

    // Re-index
    reindexBtn?.addEventListener('click', async () => {
      reindexBtn.disabled = true;
      reindexBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Re-indexing…';
      try {
        if (!APP_CONFIG.isDemoMode()) {
          await API.reindexDocuments();
          TOAST.show('Re-indexing started', 'success');
        } else {
          await delay(1500);
          TOAST.show('Re-index complete (demo mode)', 'success');
        }
      } catch (e) {
        TOAST.show(`Re-index failed: ${e.message}`, 'error');
      }
      reindexBtn.disabled = false;
      reindexBtn.innerHTML = '<i class="fas fa-sync-alt"></i> Re-index All';
    });

    loadDocuments();
  }

  async function loadDocuments() {
    try {
      if (APP_CONFIG.isDemoMode()) {
        allDocs = APP_CONFIG.get(APP_CONFIG.KEYS.DOCUMENTS, []);
      } else {
        const resp = await API.getDocuments();
        allDocs = resp?.documents || [];
      }
    } catch {
      allDocs = APP_CONFIG.get(APP_CONFIG.KEYS.DOCUMENTS, []);
    }
    renderDocsTable(docsSearch?.value || '');
  }

  function renderDocsTable(filter = '') {
    const lower = filter.toLowerCase();
    const filtered = allDocs.filter(d => d.name?.toLowerCase().includes(lower));
    if (docCount) docCount.textContent = `${filtered.length} document${filtered.length !== 1 ? 's' : ''}`;
    if (!docsTbody) return;

    if (filtered.length === 0) {
      docsTbody.innerHTML = '<tr class="empty-row"><td colspan="7">No documents found</td></tr>';
      return;
    }

    docsTbody.innerHTML = filtered.map(doc => `
      <tr>
        <td><span class="truncate" title="${escHtml(doc.name)}">${escHtml(doc.name)}</span></td>
        <td><span class="pill queued">${escHtml(doc.type || 'TXT')}</span></td>
        <td>${formatBytes(doc.size || 0)}</td>
        <td>${doc.chunks || '—'}</td>
        <td><span class="pill ${doc.status || 'indexed'}">${capitalize(doc.status || 'Indexed')}</span></td>
        <td>${formatDate(doc.uploaded_at || doc.created_at)}</td>
        <td>
          <button class="table-action-btn del" data-id="${escHtml(doc.id)}" title="Delete document">
            <i class="fas fa-trash-alt"></i>
          </button>
        </td>
      </tr>
    `).join('');

    // Delete handlers
    docsTbody.querySelectorAll('.table-action-btn.del').forEach(btn => {
      btn.addEventListener('click', () => deleteDoc(btn.dataset.id));
    });
  }

  async function handleFiles(files) {
    const allowed = ['application/pdf', 'text/plain', 'text/markdown',
                     'text/csv', 'application/vnd.ms-excel',
                     'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'];
    const allowedExts = ['.pdf','.txt','.md','.csv','.xlsx','.xls'];

    const valid = files.filter(f => {
      const ext = '.' + f.name.split('.').pop().toLowerCase();
      return allowed.includes(f.type) || allowedExts.includes(ext);
    });

    if (valid.length === 0) { TOAST.show('No supported files selected', 'warning'); return; }

    progressArea?.classList.remove('hidden');

    for (const file of valid) {
      await uploadSingleFile(file);
    }

    setTimeout(() => progressArea?.classList.add('hidden'), 3000);
    await loadDocuments();
  }

  async function uploadSingleFile(file) {
    const itemEl = createProgressItem(file);
    progressArea?.appendChild(itemEl);

    const fill   = itemEl.querySelector('.upload-bar-fill');
    const status = itemEl.querySelector('.upload-item-status');

    try {
      if (APP_CONFIG.isDemoMode()) {
        // Simulate upload in demo mode
        for (let p = 0; p <= 100; p += 10) {
          await delay(80);
          if (fill) fill.style.width = p + '%';
        }
        const doc = {
          id: APP_CONFIG.generateSessionId(),
          name: file.name,
          type: file.name.split('.').pop().toUpperCase(),
          size: file.size,
          chunks: Math.floor(file.size / 800) + 1,
          status: 'indexed',
          uploaded_at: new Date().toISOString(),
        };
        const docs = APP_CONFIG.get(APP_CONFIG.KEYS.DOCUMENTS, []);
        docs.push(doc);
        APP_CONFIG.set(APP_CONFIG.KEYS.DOCUMENTS, docs);
      } else {
        await API.uploadFile(file, p => { if (fill) fill.style.width = p + '%'; });
      }

      if (status) { status.textContent = 'Done ✓'; status.className = 'upload-item-status done'; }
      TOAST.show(`"${file.name}" uploaded successfully`, 'success');
    } catch (e) {
      if (status) { status.textContent = 'Error'; status.className = 'upload-item-status error'; }
      TOAST.show(`Upload failed: ${e.message}`, 'error');
    }
  }

  function createProgressItem(file) {
    const div = document.createElement('div');
    div.className = 'upload-item';
    div.innerHTML = `
      <span class="upload-item-name" title="${escHtml(file.name)}">${escHtml(file.name)}</span>
      <span class="upload-item-size">${formatBytes(file.size)}</span>
      <div class="upload-bar-wrap"><div class="upload-bar-fill" style="width:0%"></div></div>
      <span class="upload-item-status">Uploading…</span>
    `;
    return div;
  }

  async function deleteDoc(id) {
    if (!confirm('Delete this document from the knowledge base?')) return;
    try {
      if (!APP_CONFIG.isDemoMode()) {
        await API.deleteDocument(id);
      } else {
        const docs = APP_CONFIG.get(APP_CONFIG.KEYS.DOCUMENTS, []);
        APP_CONFIG.set(APP_CONFIG.KEYS.DOCUMENTS, docs.filter(d => d.id !== id));
      }
      TOAST.show('Document deleted', 'success');
      await loadDocuments();
    } catch (e) {
      TOAST.show(`Delete failed: ${e.message}`, 'error');
    }
  }

  // ══════════════════════════════════════════════════════════════
  // ANALYTICS
  // ══════════════════════════════════════════════════════════════
  let analyticsCharts = {};

  function initAnalytics() {
    document.getElementById('analytics-range')?.addEventListener('change', loadAnalytics);
    document.getElementById('export-analytics-btn')?.addEventListener('click', exportAnalytics);
  }

  async function loadAnalytics() {
    const days    = parseInt(document.getElementById('analytics-range')?.value || '30');
    const convs   = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, []);
    const an      = APP_CONFIG.get(APP_CONFIG.KEYS.ANALYTICS, { queries: 0, totalTime: 0 });

    const cutoff  = new Date(Date.now() - days * 86400000);
    const filtered = convs.filter(c => new Date(c.timestamp) >= cutoff);

    const positives = filtered.filter(c => c.rating === 1).length;
    const total     = filtered.length;

    // KPIs
    const avgTime = total > 0 ? ((an.totalTime || 0) / convs.length / 1000).toFixed(2) : '—';
    document.getElementById('an-total')?.setAttribute('data-v', total);
    countUp('an-total', total);
    document.getElementById('an-avg-time').textContent = avgTime;
    document.getElementById('an-satisfaction').textContent = total > 0 ? Math.round(positives / total * 100) + '%' : '—';
    document.getElementById('an-errors').textContent = '0%'; // demo

    // Charts
    renderDailyQueriesChart(filtered, days);
    renderCategoriesChart(filtered);
    renderResponseTimeChart();
    renderTopQuestions(filtered);
  }

  function renderDailyQueriesChart(convs, days) {
    const canvas = document.getElementById('chart-daily-queries');
    if (!canvas) return;

    const labels = [];
    const data   = [];

    for (let i = days - 1; i >= 0; i--) {
      const date = new Date(Date.now() - i * 86400000);
      const key  = date.toISOString().split('T')[0];
      labels.push(date.toLocaleDateString([], { month: 'short', day: 'numeric' }));
      data.push(convs.filter(c => c.timestamp?.startsWith(key)).length);
    }

    if (analyticsCharts.daily) analyticsCharts.daily.destroy();
    analyticsCharts.daily = new Chart(canvas, {
      type: 'line',
      data: {
        labels,
        datasets: [{
          label: 'Queries',
          data,
          borderColor: '#4F46E5',
          backgroundColor: 'rgba(79,70,229,0.1)',
          fill: true,
          tension: 0.4,
          pointRadius: 3,
          borderWidth: 2,
        }],
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: { beginAtZero: true, ticks: { stepSize: 1 } },
          x: { ticks: { maxTicksLimit: 10 } },
        },
      },
    });
  }

  function renderCategoriesChart(convs) {
    const canvas = document.getElementById('chart-categories');
    if (!canvas) return;

    const cats = { Shipping: 0, Returns: 0, Products: 0, Orders: 0, General: 0 };
    convs.forEach(c => {
      const m = (c.user_message || '').toLowerCase();
      if (m.includes('ship') || m.includes('deliver')) cats.Shipping++;
      else if (m.includes('return') || m.includes('refund')) cats.Returns++;
      else if (m.includes('product') || m.includes('item')) cats.Products++;
      else if (m.includes('order') || m.includes('track')) cats.Orders++;
      else cats.General++;
    });

    if (analyticsCharts.categories) analyticsCharts.categories.destroy();
    analyticsCharts.categories = new Chart(canvas, {
      type: 'pie',
      data: {
        labels: Object.keys(cats),
        datasets: [{
          data: Object.values(cats),
          backgroundColor: ['#4F46E5','#10B981','#F59E0B','#EF4444','#6366F1'],
          borderWidth: 2,
          borderColor: getComputedStyle(document.body).getPropertyValue('--surface'),
        }],
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { position: 'bottom', labels: { font: { size: 11 } } } },
      },
    });
  }

  function renderResponseTimeChart() {
    const canvas = document.getElementById('chart-response-time');
    if (!canvas) return;

    const buckets = ['<1s','1-2s','2-3s','3-5s','>5s'];
    const vals    = [15, 35, 28, 14, 8].map(v => Math.round(v + (Math.random() - .5) * 4));

    if (analyticsCharts.respTime) analyticsCharts.respTime.destroy();
    analyticsCharts.respTime = new Chart(canvas, {
      type: 'bar',
      data: {
        labels: buckets,
        datasets: [{
          label: 'Queries',
          data: vals,
          backgroundColor: ['#10B981','#34D399','#FBBf24','#F97316','#EF4444'],
          borderRadius: 4,
        }],
      },
      options: {
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: { y: { beginAtZero: true } },
      },
    });
  }

  function renderTopQuestions(convs) {
    const container = document.getElementById('top-questions-list');
    if (!container) return;

    const freq = {};
    convs.forEach(c => {
      const msg = (c.user_message || '').trim();
      if (msg) freq[msg] = (freq[msg] || 0) + 1;
    });

    const top = Object.entries(freq)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 8);

    if (top.length === 0) {
      container.innerHTML = '<p style="color:var(--text-3);font-size:.85rem;padding:.5rem 0">No data yet</p>';
      return;
    }

    container.innerHTML = top.map(([q, c], i) => `
      <div class="top-question-item">
        <span class="tq-rank">${i + 1}</span>
        <span class="tq-text" title="${escHtml(q)}">${escHtml(q)}</span>
        <span class="tq-count">${c}×</span>
      </div>
    `).join('');
  }

  function countUp(id, target) {
    const el = document.getElementById(id);
    if (!el) return;
    let start = 0;
    const step = Math.ceil(target / 30);
    const timer = setInterval(() => {
      start = Math.min(start + step, target);
      el.textContent = start;
      if (start >= target) clearInterval(timer);
    }, 30);
  }

  function exportAnalytics() {
    const convs = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, []);
    const csv = [
      ['Session ID','User Message','Bot Response','Rating','Timestamp'],
      ...convs.map(c => [c.session_id, c.user_message, c.bot_response, c.rating ?? '', c.timestamp]),
    ].map(r => r.map(f => `"${String(f || '').replace(/"/g, '""')}"`).join(',')).join('\n');

    downloadCsv(csv, 'analytics_export.csv');
    TOAST.show('Analytics exported', 'success');
  }

  // ══════════════════════════════════════════════════════════════
  // CONVERSATIONS
  // ══════════════════════════════════════════════════════════════
  let convPage = 1;

  function initConversations() {
    document.getElementById('conv-search')?.addEventListener('input', debounce(() => {
      convPage = 1;
      loadConversations();
    }, 350));
    document.getElementById('export-conv-btn')?.addEventListener('click', exportAnalytics);

    // Detail modal
    document.getElementById('close-detail-modal')?.addEventListener('click', () => {
      document.getElementById('detail-modal')?.classList.add('hidden');
    });
    document.getElementById('detail-modal')?.addEventListener('click', e => {
      if (e.target === document.getElementById('detail-modal'))
        document.getElementById('detail-modal')?.classList.add('hidden');
    });
  }

  async function loadConversations() {
    const search  = document.getElementById('conv-search')?.value || '';
    const convs   = APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, [])
      .filter(c => !search || c.user_message?.toLowerCase().includes(search.toLowerCase()))
      .reverse();

    const perPage = 20;
    const total   = convs.length;
    const paged   = convs.slice((convPage - 1) * perPage, convPage * perPage);

    const countEl = document.getElementById('conv-count');
    if (countEl) countEl.textContent = `${total} conversation${total !== 1 ? 's' : ''}`;

    const tbody = document.getElementById('conv-tbody');
    if (!tbody) return;

    if (paged.length === 0) {
      tbody.innerHTML = '<tr class="empty-row"><td colspan="6">No conversations found</td></tr>';
    } else {
      tbody.innerHTML = paged.map(c => `
        <tr>
          <td><code style="font-size:.75rem">${escHtml((c.session_id || '').split('-')[0])}</code></td>
          <td><span class="truncate" style="max-width:200px" title="${escHtml(c.user_message)}">${escHtml(c.user_message)}</span></td>
          <td><span class="truncate" style="max-width:220px" title="${escHtml(c.bot_response)}">${escHtml(c.bot_response)}</span></td>
          <td>${c.rating === 1 ? '👍' : c.rating === -1 ? '👎' : '—'}</td>
          <td style="white-space:nowrap">${formatDate(c.timestamp)}</td>
          <td>
            <button class="table-action-btn view-conv-btn" data-id="${escHtml(c.id)}" title="View full conversation">
              <i class="fas fa-eye"></i>
            </button>
          </td>
        </tr>
      `).join('');

      tbody.querySelectorAll('.view-conv-btn').forEach(btn => {
        btn.addEventListener('click', () => showConvDetail(btn.dataset.id));
      });
    }

    // Pagination
    renderPagination('conv-pagination', convPage, Math.ceil(total / perPage), p => {
      convPage = p; loadConversations();
    });
  }

  function showConvDetail(id) {
    const conv = (APP_CONFIG.get(APP_CONFIG.KEYS.CONVERSATIONS, [])).find(c => c.id === id);
    if (!conv) return;

    const body = document.getElementById('detail-modal-body');
    if (body) {
      body.innerHTML = `
        <div class="conv-detail-turn">
          <div class="conv-detail-role user"><i class="fas fa-user"></i> User</div>
          <div class="conv-detail-content">${escHtml(conv.user_message)}</div>
        </div>
        <div class="conv-detail-turn">
          <div class="conv-detail-role bot"><i class="fas fa-robot"></i> Assistant</div>
          <div class="conv-detail-content">${escHtml(conv.bot_response)}</div>
        </div>
        <div style="margin-top:1rem; font-size:.8rem; color:var(--text-3)">
          <strong>Session:</strong> ${escHtml(conv.session_id || '')} &nbsp;|&nbsp;
          <strong>Rating:</strong> ${conv.rating === 1 ? '👍 Helpful' : conv.rating === -1 ? '👎 Not helpful' : 'No rating'} &nbsp;|&nbsp;
          <strong>Time:</strong> ${formatDate(conv.timestamp)}
        </div>
      `;
    }
    document.getElementById('detail-modal')?.classList.remove('hidden');
  }

  // ══════════════════════════════════════════════════════════════
  // CONFIGURATION
  // ══════════════════════════════════════════════════════════════
  function initConfiguration() {
    const settings = APP_CONFIG.getRagSettings();
    const businessName = APP_CONFIG.getBusinessName();
    const backendUrl   = APP_CONFIG.getBackendUrl();

    // Pre-fill fields
    setValue('cfg-chunk-size',    settings.chunkSize);
    setValue('cfg-chunk-overlap', settings.chunkOverlap);
    setValue('cfg-top-k',         settings.topK);
    setValue('cfg-similarity',    settings.similarity);
    setValue('cfg-model',         settings.model);
    setValue('cfg-max-tokens',    settings.maxTokens);
    setValue('cfg-memory',        settings.memoryTurns);
    setValue('cfg-business-name', businessName);
    setValue('cfg-backend-url',   backendUrl);

    const tempInput   = document.getElementById('cfg-temperature');
    const tempDisplay = document.getElementById('temperature-display');
    if (tempInput) {
      tempInput.value = settings.temperature;
      if (tempDisplay) tempDisplay.textContent = settings.temperature;
      tempInput.addEventListener('input', () => {
        if (tempDisplay) tempDisplay.textContent = tempInput.value;
      });
    }

    // Test backend
    document.getElementById('test-backend-btn')?.addEventListener('click', async () => {
      const url = document.getElementById('cfg-backend-url')?.value?.trim() || '';
      const resultEl = document.getElementById('backend-test-result');
      if (resultEl) resultEl.className = 'test-result checking';
      if (resultEl) resultEl.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Testing connection…';
      resultEl?.classList.remove('hidden');

      if (!url) {
        resultEl.className = 'test-result';
        resultEl.innerHTML = '<i class="fas fa-info-circle"></i> Demo mode (no URL)';
        return;
      }

      const res = await API.testConnection(url);
      if (resultEl) {
        resultEl.className = `test-result ${res.ok ? 'success' : 'error'}`;
        resultEl.innerHTML = res.ok
          ? `<i class="fas fa-check-circle"></i> Connected! ${res.version ? `Version: ${res.version}` : ''}`
          : `<i class="fas fa-times-circle"></i> Failed: ${res.msg}`;
      }
    });

    // Save all settings
    document.getElementById('save-config-btn')?.addEventListener('click', saveAllSettings);
  }

  async function saveAllSettings() {
    const settings = {
      chunkSize:    parseInt(document.getElementById('cfg-chunk-size')?.value || 800),
      chunkOverlap: parseInt(document.getElementById('cfg-chunk-overlap')?.value || 150),
      topK:         parseInt(document.getElementById('cfg-top-k')?.value || 5),
      similarity:   parseFloat(document.getElementById('cfg-similarity')?.value || 0.7),
      model:        document.getElementById('cfg-model')?.value || 'gpt-4o-mini',
      temperature:  parseFloat(document.getElementById('cfg-temperature')?.value || 0.3),
      maxTokens:    parseInt(document.getElementById('cfg-max-tokens')?.value || 500),
      memoryTurns:  parseInt(document.getElementById('cfg-memory')?.value || 5),
    };

    APP_CONFIG.saveRagSettings(settings);
    APP_CONFIG.setBusinessName(document.getElementById('cfg-business-name')?.value || 'ShopBot AI');
    APP_CONFIG.setBackendUrl(document.getElementById('cfg-backend-url')?.value || '');

    const btn = document.getElementById('save-config-btn');
    if (btn) { btn.disabled = true; btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving…'; }

    try {
      if (!APP_CONFIG.isDemoMode()) {
        await API.saveConfig({ ...settings, systemPrompt: document.getElementById('cfg-system-prompt')?.value });
      }
      TOAST.show('Settings saved successfully!', 'success');
    } catch {
      TOAST.show('Settings saved locally (backend unreachable)', 'warning');
    }

    if (btn) { btn.disabled = false; btn.innerHTML = '<i class="fas fa-save"></i> Save All Settings'; }
  }

  // ══════════════════════════════════════════════════════════════
  // UTILITIES
  // ══════════════════════════════════════════════════════════════
  function escHtml(str) {
    return String(str || '')
      .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
      .replace(/"/g,'&quot;').replace(/'/g,'&#39;');
  }

  function formatBytes(bytes) {
    if (!bytes) return '—';
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / 1024 / 1024).toFixed(1) + ' MB';
  }

  function formatDate(isoStr) {
    if (!isoStr) return '—';
    try { return new Date(isoStr).toLocaleString([], { dateStyle: 'medium', timeStyle: 'short' }); }
    catch { return isoStr; }
  }

  function capitalize(str) {
    return str ? str.charAt(0).toUpperCase() + str.slice(1) : '';
  }

  function getLast7Days() {
    return Array.from({ length: 7 }, (_, i) => {
      const d = new Date(Date.now() - (6 - i) * 86400000);
      return d.toISOString().split('T')[0];
    });
  }

  function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

  function debounce(fn, wait) {
    let t;
    return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), wait); };
  }

  function setValue(id, val) {
    const el = document.getElementById(id);
    if (el) el.value = val ?? '';
  }

  function downloadCsv(csv, filename) {
    const blob = new Blob([csv], { type: 'text/csv' });
    const url  = URL.createObjectURL(blob);
    const a    = document.createElement('a');
    a.href = url; a.download = filename; a.click();
    URL.revokeObjectURL(url);
  }

  function renderPagination(containerId, currentPage, totalPages, onPageClick) {
    const container = document.getElementById(containerId);
    if (!container || totalPages <= 1) { if (container) container.innerHTML = ''; return; }

    let html = '';
    const range = 2;
    for (let p = 1; p <= totalPages; p++) {
      if (p === 1 || p === totalPages || (p >= currentPage - range && p <= currentPage + range)) {
        html += `<button class="page-btn ${p === currentPage ? 'active' : ''}" data-p="${p}">${p}</button>`;
      } else if (p === currentPage - range - 1 || p === currentPage + range + 1) {
        html += '<span style="padding:.4rem">…</span>';
      }
    }
    container.innerHTML = html;
    container.querySelectorAll('.page-btn').forEach(btn => {
      btn.addEventListener('click', () => onPageClick(parseInt(btn.dataset.p)));
    });
  }

})();
