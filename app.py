import streamlit as st

st.set_page_config(page_title="SocialPulse \u2014 News Hub", page_icon="logo.png", layout="wide")

from styles import CSS
from data import get_articles
from templates import page_home, page_category, page_article, page_trending, page_live, page_search

if "toasts" not in st.session_state:
    st.session_state.toasts = []

st.html(f"<style>{CSS}</style>")

st.html("""
<div id="loading-spinner">
  <div class="spinner-ring"></div>
</div>
<style>
#loading-spinner{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;background:#0a0a1a;transition:opacity .3s ease;pointer-events:none;}
#loading-spinner.hide{opacity:0;}
.spinner-ring{width:48px;height:48px;border:4px solid rgba(167,139,250,0.15);border-top-color:#a78bfa;border-radius:50%;animation:spin-ring .8s linear infinite;}
@keyframes spin-ring{to{transform:rotate(360deg)}}
</style>
<script>requestAnimationFrame(function(){var n=document.getElementById('loading-spinner');if(n){n.classList.add('hide');setTimeout(function(){n.remove()},400);}});</script>
""", unsafe_allow_javascript=True)

st.session_state.page = st.query_params.get("page", "home")
st.session_state.cat = st.query_params.get("cat", "All")
st.session_state.aid = st.query_params.get("id", None)
st.session_state.q = st.query_params.get("q", "")

meta_title = "SocialPulse \u2014 News Hub"
meta_desc = "Real-time news aggregator covering Tech, AI, Business, World, Science, Entertainment, and Social Media."
if st.session_state.page == "category" and st.session_state.cat:
    meta_title = f"{st.session_state.cat} - SocialPulse"

st.html(f"""
<meta property="og:title" content="{meta_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
""")

st.html("""
<script>
(function() {
  document.addEventListener('keydown', function(e) {
    if (e.key === '/' && !e.ctrlKey && !e.metaKey) {
      const tag = document.activeElement?.tagName;
      if (tag !== 'INPUT' && tag !== 'TEXTAREA') {
        e.preventDefault();
        const inp = document.querySelector('.search-input');
        if (inp) { inp.focus(); inp.click(); }
      }
    }
  });
  window.addEventListener('scroll', function() {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    const pct = h > 0 ? (window.scrollY / h * 100) : 0;
    const bar = document.getElementById('rdr-progress');
    if (bar) bar.style.width = pct + '%';
  });
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(function() {});
  }
})();
</script>
""", unsafe_allow_javascript=True)

articles = get_articles(24)

page = st.session_state.page
cat = st.session_state.cat
aid = st.session_state.aid

try:
    if page == "article" and aid is not None:
        page_article(articles, int(aid))
    elif page == "category":
        page_category(articles, cat)
    elif page == "trending":
        page_trending(articles)
    elif page == "live":
        page_live()
    elif page == "search":
        page_search(articles)
    else:
        page_home(articles)
except Exception:
    st.session_state.page = "home"
    st.rerun()