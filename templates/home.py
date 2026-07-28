import streamlit as st
from datetime import datetime
from components.nav import render_nav
from components.cards import render_article_grid, render_section_header, render_breaking
from components.ui import render_footer, render_toasts
from data.fetcher import gen_live_feed
from config.settings import TRENDING_TOPICS
import random


def _live_feed_sidebar():
    feed = gen_live_feed(12)
    items_html = "".join(
        f"""<a href="?page=live" target="_self" style="text-decoration:none;display:block;">
            <div class="timeline-item" style="cursor:pointer;">
                <div class="timeline-dot" style="background:{item['color']};"></div>
                <div class="timeline-body"><div class="t">{item['text']}</div><div class="s">{item['time'].strftime("%I:%M %p")}</div></div>
            </div></a>"""
        for item in feed[:6]
    )
    st.html(f"""<div class="glass" style="padding:1rem 1.2rem;">
        <div style="font-size:0.85rem;font-weight:600;color:var(--text);margin-bottom:0.3rem;">\u23f1 Live Feed</div>
        {items_html}
    </div>""")


def _trending_sidebar():
    dots = ["#6366f1", "#ec4899", "#34d399", "#f59e0b", "#14b8a6", "#8b5cf6", "#ef4444", "#0ea5e9"]
    items_html = "".join(
        f"""<a href="?page=trending" target="_self" style="text-decoration:none;display:block;">
            <div class="trend-item" style="cursor:pointer;">
                <div class="trend-num">#{i + 1}</div>
                <div class="trend-text"><div class="t">{t}</div><div class="s">{random.randint(1200, 85000):,} posts</div></div>
                <div class="trend-dot" style="background:{dots[i]};"></div>
            </div></a>"""
        for i, t in enumerate(TRENDING_TOPICS[:6])
    )
    st.html(f"""<div class="glass" style="padding:1rem 1.2rem;">
        <div style="font-size:0.85rem;font-weight:600;color:var(--text);margin-bottom:0.3rem;">Trending</div>
        {items_html}
    </div>""")


def page_home(articles):
    render_nav("home")
    bi = int(datetime.now().timestamp() / 180) % 12
    render_breaking(bi)
    trend_col, main_col = st.columns([1, 3.5])
    with trend_col:
        _trending_sidebar()
        st.html("<br>")
        st.html('<div class="sub-box"><h3>\U0001f4ec Stay Updated</h3><p>Get the latest news daily.</p></div>')
        st.html("<br>")
        _live_feed_sidebar()
    with main_col:
        sections = [
            ("\U0001f4f0 Latest News", articles[:9], "?page=category&cat=All"),
            ("\U0001f4f1 Social Media", [a for a in articles if a["cat"] == "Social Media"][:6], "?page=category&cat=Social%20Media"),
            ("\U0001f30d World", [a for a in articles if a["cat"] == "World"][:6], "?page=category&cat=World"),
            ("\U0001f4bb Tech", [a for a in articles if a["cat"] == "Tech"][:6], "?page=category&cat=Tech"),
            ("\U0001f916 AI & Science", [a for a in articles if a["cat"] in ("AI", "Science")][:6], "?page=category&cat=AI"),
            ("\U0001f4ca Business", [a for a in articles if a["cat"] == "Business"][:6], "?page=category&cat=Business"),
            ("\U0001f3ac Entertainment", [a for a in articles if a["cat"] == "Entertainment"][:6], "?page=category&cat=Entertainment"),
        ]
        for title, items, link in sections:
            if items:
                render_section_header(title, link)
                render_article_grid(items[:6])
    render_footer()
    render_toasts()