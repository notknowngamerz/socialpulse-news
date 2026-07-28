CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');

* { font-family: 'Inter', sans-serif; margin:0; padding:0; box-sizing:border-box; }

html { scroll-behavior: smooth; }

:root {
  --bg: #0a0a1a;
  --bg-alt: #12122a;
  --surface: rgba(255,255,255,0.05);
  --surface-hover: rgba(255,255,255,0.08);
  --border: rgba(255,255,255,0.07);
  --border-hover: rgba(255,255,255,0.1);
  --text: #fff;
  --text-secondary: rgba(255,255,255,0.45);
  --text-tertiary: rgba(255,255,255,0.25);
  --accent: #a78bfa;
  --accent2: #6366f1;
  --accent3: #ec4899;
  --glass-bg: rgba(255,255,255,0.05);
  --nav-bg: transparent;
  --shadow: rgba(0,0,0,0.35);
  --scrollbar: rgba(255,255,255,0.08);
  --scrollbar-hover: rgba(255,255,255,0.15);
  --focus-ring: rgba(167,139,250,0.3);
  --overlay-dark: rgba(0,0,0,0.85);
}

body { background:var(--bg); }
.stApp { background:var(--bg); background-image:radial-gradient(ellipse at 20% 50%,rgba(99,102,241,0.04) 0%,transparent 60%),radial-gradient(ellipse at 80% 50%,rgba(236,72,153,0.03) 0%,transparent 60%); }
.stApp::before { content:""; position:fixed; inset:0; background:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.015'/%3E%3C/svg%3E"); pointer-events:none; z-index:0; }

section[data-testid="stSidebar"] { display:none; }
header[data-testid="stHeader"] { display:none; }
#MainMenu, footer { visibility:hidden; }
.stApp > header { display:none !important; }
.main .block-container { padding:0 2rem; max-width:1440px; position:relative; z-index:1; }

::-webkit-scrollbar { width:6px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:var(--scrollbar); border-radius:10px; }
::-webkit-scrollbar-thumb:hover { background:var(--scrollbar-hover); }

@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }
.main .block-container { animation:fadeIn .35s ease-out; }

.glass { background:var(--glass-bg); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border:1px solid var(--border); border-radius:18px; color:var(--text); transition:transform .3s cubic-bezier(.22,1,.36,1), box-shadow .3s ease, background .3s ease; overflow:hidden; }
.glass:hover { transform:translateY(-3px); box-shadow:0 14px 44px var(--shadow); }

.article-grid { display:grid; grid-template-columns:repeat(var(--cols,3),1fr); gap:1rem; }

.nav { display:flex; justify-content:space-between; align-items:center; padding:0.75rem 1.5rem; border-bottom:1px solid var(--border); margin-bottom:1.5rem; background:var(--nav-bg); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); position:sticky; top:0; z-index:100; border-radius:0 0 18px 18px; transition:background .3s ease; }
.nav-brand { display:flex; align-items:center; gap:10px; font-size:1.35rem; font-weight:800; background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; cursor:pointer; }
.nav-links { display:flex; gap:0.3rem; flex-wrap:wrap; }
.nav-links a { color:var(--text-secondary); text-decoration:none; font-size:0.82rem; padding:0.35rem 1rem; border-radius:30px; transition:color .2s,background .2s,border-color .2s; border:1px solid transparent; cursor:pointer; position:relative; }
.nav-links a:hover { color:var(--text); background:var(--surface-hover); }
.nav-links a.active { color:var(--text); background:var(--surface-hover); border-color:var(--border-hover); }
.nav-right { display:flex; align-items:center; gap:0.8rem; }

.live-badge { display:flex; align-items:center; gap:6px; background:var(--surface); backdrop-filter:blur(12px); border:1px solid var(--border); border-radius:30px; padding:0.3rem 0.9rem; color:var(--text); font-size:0.7rem; font-weight:500; letter-spacing:0.3px; }
.live-dot { width:6px;height:6px;border-radius:50%;background:#34d399;animation:pulse-dot 1.8s ease-in-out infinite; }
@keyframes pulse-dot { 0%,100%{box-shadow:0 0 0 0 rgba(52,211,153,0.5)} 50%{box-shadow:0 0 0 8px rgba(52,211,153,0)} }
.clock { color:var(--text-tertiary); font-size:0.75rem; font-family:'JetBrains Mono',monospace; letter-spacing:0.3px; }

.breaking-wrap { margin-bottom:1.8rem; background:linear-gradient(135deg,rgba(99,102,241,0.1),rgba(236,72,153,0.06)); border:1px solid var(--border); border-radius:18px; padding:1.5rem 2rem; position:relative; overflow:hidden; cursor:pointer; transition:all .3s ease; }
.breaking-wrap:hover { border-color:rgba(167,139,250,0.2); transform:translateY(-2px); box-shadow:0 12px 40px rgba(99,102,241,0.1); }
.breaking-wrap::before { content:""; position:absolute; inset:0; background:radial-gradient(ellipse at 30% 50%,rgba(167,139,250,0.1),transparent 60%); pointer-events:none; }
.breaking-label { display:inline-block; background:linear-gradient(135deg,#ef4444,#ec4899); color:#fff; font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:1.8px; padding:0.2rem 0.8rem; border-radius:6px; margin-bottom:0.8rem; }
.breaking-title { font-size:1.5rem; font-weight:700; color:var(--text); line-height:1.3; margin-bottom:0.5rem; }
.breaking-meta { display:flex; align-items:center; gap:1rem; color:var(--text-tertiary); font-size:0.75rem; }
.breaking-meta .src { color:var(--accent); font-weight:500; }

.article-card { background:var(--glass-bg); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border:1px solid var(--border); border-radius:18px; overflow:hidden; transition:transform .35s cubic-bezier(.22,1,.36,1), box-shadow .35s ease, background .3s ease; height:100%; display:flex; flex-direction:column; cursor:pointer; position:relative; will-change:transform; content-visibility:auto; contain-intrinsic-size:400px; }
.article-card:hover { transform:translateY(-5px); box-shadow:0 16px 48px var(--shadow); }
.article-img { height:200px; width:100%; position:relative; overflow:hidden; display:flex; align-items:flex-end; padding:1rem; background-size:cover; background-position:center; transition:transform .4s ease; background-color:var(--bg-alt); will-change:transform; content-visibility:auto; }
.article-card:hover .article-img { transform:scale(1.03); }
.article-img::after { content:""; position:absolute; bottom:0; left:0; right:0; height:70%; background:linear-gradient(transparent 15%,rgba(0,0,0,0.8) 90%); pointer-events:none; }
.article-img .img-tag { font-size:0.6rem; font-weight:600; text-transform:uppercase; letter-spacing:0.8px; padding:0.2rem 0.7rem; border-radius:6px; backdrop-filter:blur(12px); background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); position:relative; z-index:1; }
.article-img .img-source { position:absolute; top:0.8rem; right:0.8rem; z-index:1; font-size:0.55rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; padding:0.2rem 0.6rem; border-radius:5px; background:rgba(0,0,0,0.3); backdrop-filter:blur(8px); border:1px solid rgba(255,255,255,0.07); color:rgba(255,255,255,0.65); }

.article-body { padding:1rem 1.2rem 1.2rem; flex:1; display:flex; flex-direction:column; }
.article-body .cat { font-size:0.6rem; font-weight:600; text-transform:uppercase; letter-spacing:0.8px; color:var(--accent); margin-bottom:0.3rem; }
.article-body .title { font-size:1rem; font-weight:600; color:var(--text); line-height:1.35; margin-bottom:0.35rem; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }
.article-body .desc { font-size:0.78rem; color:var(--text-secondary); line-height:1.5; margin-bottom:0.7rem; flex:1; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }
.article-body .meta { display:flex; justify-content:space-between; align-items:center; font-size:0.68rem; color:var(--text-tertiary); padding-top:0.5rem; border-top:1px solid var(--border); gap:0.5rem; }
.article-body .meta .left { display:flex; align-items:center; gap:0.6rem; flex:1; min-width:0; }
.article-body .meta .source { color:var(--text-secondary); font-weight:500; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.article-body .meta .right { display:flex; align-items:center; gap:0.6rem; flex-shrink:0; }

@keyframes shimmer { 0%{background-position:-400px 0} 100%{background-position:400px 0} }
.skeleton { background:linear-gradient(90deg,var(--surface) 25%,var(--surface-hover) 50%,var(--surface) 75%); background-size:800px 100%; animation:shimmer 1.5s ease-in-out infinite; border-radius:8px; }
.skeleton-img { height:200px; width:100%; border-radius:18px 18px 0 0; }
.skeleton-line { height:14px; margin-bottom:8px; width:100%; }
.skeleton-line:last-child { width:60%; }
.skeleton-cat { height:12px; width:80px; margin-bottom:10px; }
.skeleton-body { padding:1rem 1.2rem; }

.toast-container { position:fixed; bottom:24px; right:24px; z-index:9999; display:flex; flex-direction:column; gap:8px; }
.toast { padding:0.6rem 1.2rem; border-radius:12px; font-size:0.8rem; font-weight:500; backdrop-filter:blur(16px); box-shadow:0 8px 24px var(--shadow); animation:toast-in .3s ease-out; display:flex; align-items:center; gap:8px; }
.toast-success { background:rgba(52,211,153,0.15); border:1px solid rgba(52,211,153,0.3); color:#34d399; }
.toast-info { background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); color:#a78bfa; }
.toast-error { background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); color:#f87171; }
@keyframes toast-in { from{transform:translateX(100px);opacity:0} to{transform:translateX(0);opacity:1} }

.progress-bar { position:fixed; top:0; left:0; height:3px; background:linear-gradient(90deg,var(--accent2),var(--accent3)); z-index:10001; transition:width .1s linear; border-radius:0 3px 3px 0; }

.status-new { display:inline-flex; align-items:center; gap:3px; font-size:0.6rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; padding:0.15rem 0.45rem; border-radius:4px; background:rgba(52,211,153,0.12); color:#34d399; }
.status-hot { display:inline-flex; align-items:center; gap:3px; font-size:0.6rem; font-weight:600; text-transform:uppercase; letter-spacing:0.5px; padding:0.15rem 0.45rem; border-radius:4px; background:rgba(239,68,68,0.12); color:#f87171; }

.section-header { display:flex; justify-content:space-between; align-items:center; margin:2rem 0 1rem; }
.section-header h2 { font-size:1.15rem; font-weight:700; color:var(--text); display:flex; align-items:center; gap:0.6rem; }
.section-header .see-all { font-size:0.75rem; color:var(--text-tertiary); cursor:pointer; transition:color .2s; text-decoration:none; }
.section-header .see-all:hover { color:var(--accent); }

.trend-item { display:flex; align-items:center; gap:0.8rem; padding:0.6rem 0; border-bottom:1px solid var(--border); cursor:pointer; transition:all .2s; }
.trend-item:last-child { border-bottom:none; }
.trend-item:hover .t { color:var(--accent); }
.trend-num { font-size:1rem; font-weight:800; color:var(--text-tertiary); min-width:22px; font-family:'JetBrains Mono',monospace; }
.trend-text { flex:1; min-width:0; }
.trend-text .t { font-size:0.82rem; color:var(--text); font-weight:500; transition:color .2s; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.trend-text .s { font-size:0.65rem; color:var(--text-tertiary); margin-top:1px; }
.trend-dot { width:5px;height:5px;border-radius:50%; flex-shrink:0; }

.timeline-item { display:flex; gap:0.8rem; padding:0.6rem 0; border-bottom:1px solid var(--border); }
.timeline-item:last-child { border-bottom:none; }
.timeline-dot { width:7px;height:7px;border-radius:50%; margin-top:3px; flex-shrink:0; }
.timeline-body { flex:1; min-width:0; }
.timeline-body .t { font-size:0.8rem; color:var(--text); line-height:1.4; }
.timeline-body .s { font-size:0.65rem; color:var(--text-tertiary); margin-top:2px; }

.sub-box { background:linear-gradient(135deg,rgba(99,102,241,0.08),rgba(236,72,153,0.04)); border:1px solid var(--border); border-radius:18px; padding:1.3rem; text-align:center; }
.sub-box h3 { font-size:0.95rem; font-weight:600; color:var(--text); margin-bottom:0.2rem; }
.sub-box p { font-size:0.72rem; color:var(--text-secondary); margin-bottom:0; }

.footer { text-align:center; padding:2rem 0 1rem; border-top:1px solid var(--border); margin-top:2.5rem; color:var(--text-tertiary); font-size:0.68rem; }

.search-input { background:var(--surface); border:1px solid var(--border); border-radius:30px; padding:0.35rem 0.8rem 0.35rem 1rem; color:var(--text); font-size:0.75rem; outline:none; width:160px; transition:all .25s; }
.search-input:focus { border-color:var(--focus-ring); width:200px; background:var(--surface-hover); }
.search-input::placeholder { color:var(--text-tertiary); }

.back-btn { display:inline-flex; align-items:center; gap:6px; color:var(--text-secondary); text-decoration:none; font-size:0.8rem; padding:0.3rem 1rem; border-radius:30px; background:var(--surface); backdrop-filter:blur(12px); border:1px solid var(--border); cursor:pointer; transition:all .2s; margin-bottom:1.5rem; }
.back-btn:hover { color:var(--text); background:var(--surface-hover); border-color:var(--border-hover); }

.detail-img { width:100%; height:420px; border-radius:18px; background-size:cover; background-position:center; position:relative; margin-bottom:2rem; overflow:hidden; background-color:var(--bg-alt); }
.detail-img::after { content:""; position:absolute; bottom:0; left:0; right:0; height:65%; background:linear-gradient(transparent,var(--overlay-dark)); pointer-events:none; }
.detail-img .detail-overlay { position:absolute; bottom:2rem; left:2rem; right:2rem; z-index:2; }
.detail-img .detail-tag { display:inline-block; font-size:0.6rem; font-weight:600; text-transform:uppercase; letter-spacing:0.8px; padding:0.2rem 0.7rem; border-radius:6px; backdrop-filter:blur(12px); background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1); color:#fff; margin-bottom:0.8rem; }
.detail-img h1 { font-size:1.9rem; font-weight:700; color:#fff; line-height:1.3; }
.detail-img .detail-meta { display:flex; gap:1.2rem; margin-top:0.8rem; font-size:0.8rem; color:rgba(255,255,255,0.45); flex-wrap:wrap; }
.detail-img .detail-meta span { display:flex; align-items:center; gap:5px; }
.detail-img .detail-meta .hl { color:var(--accent); font-weight:500; }
.detail-body { font-size:0.95rem; line-height:1.85; color:var(--text-secondary); max-width:760px; margin:0 auto; transition:color .3s ease; }
.detail-body p { margin-bottom:1.2rem; }

@media (max-width:768px) {
    .nav { flex-direction:column; gap:0.8rem; padding:0.75rem 1rem; }
    .nav-links { justify-content:center; }
    .nav-right { width:100%; justify-content:center; flex-wrap:wrap; }
    .breaking-title { font-size:1.15rem; }
    .breaking-wrap { padding:1.2rem 1.2rem; }
    .main .block-container { padding:0 1rem; }
    .detail-img { height:260px; }
    .detail-img h1 { font-size:1.3rem; }
    .detail-img .detail-overlay { left:1rem; right:1rem; bottom:1.2rem; }
    .detail-img .detail-meta { gap:0.8rem; font-size:0.72rem; }
    .article-img { height:170px; }
}
"""