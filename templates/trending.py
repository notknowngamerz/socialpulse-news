import streamlit as st
import random
from datetime import datetime
from components.nav import render_nav
from components.cards import render_section_header
from components.ui import render_footer
from config.settings import TRENDING_TOPICS


def page_trending(articles=None):
    render_nav("trending")
    render_section_header("\U0001f525 Trending Topics", "#")
    dots = ["#6366f1","#ec4899","#34d399","#f59e0b","#14b8a6","#8b5cf6","#ef4444","#0ea5e9","#a78bfa","#f43f5e","#06b6d4","#d946ef"]
    vols = ["High","Very High","Moderate","High","Very High","Moderate","High","Low","Moderate","High","Low","Very High"]
    vc_map = {"High":"#f59e0b","Very High":"#ef4444","Moderate":"#34d399","Low":"rgba(255,255,255,0.25)"}
    cols = st.columns(2)
    for i, t in enumerate(TRENDING_TOPICS):
        with cols[i % 2]:
            posts = random.randint(5000, 500000)
            vc = vc_map[vols[i]]
            tags = "".join(
                f'<span style="font-size:0.65rem;padding:0.15rem 0.5rem;border-radius:20px;background:rgba(255,255,255,0.04);color:rgba(255,255,255,0.4);">{x}</span>'
                for x in random.sample(TRENDING_TOPICS, 3)
            )
            st.html(f"""
            <div class="glass" style="padding:1.2rem 1.5rem;margin-bottom:1rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.4rem;">
                    <div style="display:flex;align-items:center;gap:0.8rem;">
                        <div style="width:9px;height:9px;border-radius:50%;background:{dots[i]};"></div>
                        <span style="font-size:1.05rem;font-weight:700;color:#fff;">{t}</span>
                    </div>
                    <span style="font-size:0.65rem;font-weight:600;padding:0.15rem 0.5rem;border-radius:20px;background:{vc}18;color:{vc};">{vols[i]}</span>
                </div>
                <div style="font-size:0.78rem;color:rgba(255,255,255,0.35);">{posts:,} posts</div>
                <div style="margin-top:0.7rem;display:flex;gap:0.4rem;flex-wrap:wrap;">{tags}</div>
            </div>""")
    render_footer()