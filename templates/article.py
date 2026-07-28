import streamlit as st
from components.nav import render_nav
from components.cards import render_section_header, render_article_grid
from components.ui import render_back, render_progress_bar, render_footer, render_toasts, add_toast
from data.fetcher import get_article_by_id
from config.settings import CAT_COLORS


def page_article(articles, article_id):
    render_progress_bar()
    art = get_article_by_id(articles, article_id)
    if not art:
        art = articles[0]
    related = [a for a in articles if a["cat"] == art["cat"] and a["id"] != art["id"]][:3]
    tc = CAT_COLORS.get(art["cat"], "#a78bfa")

    render_nav("article")
    render_back()

    bmk_key = f"bm_{art['id']}"
    if bmk_key not in st.session_state:
        st.session_state[bmk_key] = False

    st.html(f"""
    <div class="detail-img" style="background-image:url('{art['img_url']}');">
        <div class="detail-overlay">
            <span class="detail-tag" style="background:{tc}22;color:{tc};border-color:{tc}33;">{art['cat']}</span>
            <h1>{art['headline']}</h1>
            <div class="detail-meta">
                <span class="hl">{art['source']}</span><span>\u00b7</span>
                <span>By {art['author']}</span><span>\u00b7</span>
                <span>{art['read_time']} min read</span><span>\u00b7</span>
                <span>{art['time'].strftime("%b %d, %Y")} \u00b7 {art['time'].strftime("%I:%M %p")}</span>
            </div>
        </div>
    </div>
    <div style="text-align:right;margin-bottom:1rem;">
        <span style="font-size:0.75rem;color:var(--text-tertiary);margin-left:0.8rem;">{art['views']:,} views</span>
    </div>
    <div class="detail-body">
        <p>{art['summary']}</p><p>{art['body']}</p>
        <p>The announcement has drawn reactions from industry leaders and analysts. Many see this as a pivotal moment that will reshape how companies approach their digital strategies moving forward.</p>
        <p>Stakeholders are closely monitoring the situation as more details emerge. Early indicators suggest strong adoption rates and positive feedback from early implementers.</p>
    </div>""")

    c1, c2 = st.columns([1, 6])
    with c1:
        bm_label = "\u2605" if st.session_state[bmk_key] else "\u2606"
        btn_text = f"{bm_label} Bookmarked" if st.session_state[bmk_key] else f"{bm_label} Bookmark"
        if st.button(btn_text, use_container_width=True, key=f"bm_btn_{art['id']}"):
            st.session_state[bmk_key] = not st.session_state[bmk_key]
            if st.session_state[bmk_key]:
                add_toast("\u2b50 Article bookmarked!")
            else:
                add_toast("Bookmark removed")
    with c2:
        if st.button("\U0001f517 Share", use_container_width=True, key=f"share_{art['id']}"):
            add_toast("\U0001f517 Link copied to clipboard", "info")

    if related:
        st.html("<br>")
        render_section_header(f"Related {art['cat']} News", f"?page=category&cat={art['cat']}")
        render_article_grid(related)
    render_footer()
    render_toasts()