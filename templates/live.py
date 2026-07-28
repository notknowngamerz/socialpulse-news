import streamlit as st
from datetime import datetime
from components.nav import render_nav
from components.cards import render_section_header
from components.ui import render_footer
from data.fetcher import gen_live_feed


@st.fragment(run_every=10)
def _live_page_fragment():
    feed = gen_live_feed(25)
    st.html(
        f'<div style="text-align:right;font-size:0.7rem;color:var(--text-tertiary);margin-bottom:1rem;'
        f'font-family:JetBrains Mono,monospace;">Updated {datetime.now().strftime("%I:%M:%S %p")}</div>'
    )
    for item in feed:
        st.html(f"""
        <div class="glass" style="padding:0.75rem 1.2rem;margin-bottom:0.4rem;display:flex;align-items:center;gap:1rem;">
            <div style="width:7px;height:7px;border-radius:50%;background:{item['color']};flex-shrink:0;"></div>
            <div style="flex:1;"><span style="color:var(--text);font-size:0.82rem;">{item['text']}</span></div>
            <div style="font-size:0.65rem;color:var(--text-tertiary);white-space:nowrap;font-family:JetBrains Mono,monospace;">{item['time'].strftime("%I:%M %p")}</div>
        </div>""")


def page_live(articles=None):
    render_nav("live")
    render_section_header("\u23f1 Live Feed", "#")
    _live_page_fragment()
    render_footer()