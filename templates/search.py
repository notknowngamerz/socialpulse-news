import streamlit as st
from components.nav import render_nav
from components.cards import render_section_header, render_article_grid
from components.ui import render_footer


def page_search(articles):
    render_nav("search")
    render_section_header("\U0001f50d Search", "#")

    with st.form("search_form", border=False):
        c1, c2 = st.columns([5, 1])
        with c1:
            q = st.session_state.get("q", "")
            sq = st.text_input("", value=q, placeholder="Search articles, topics, sources... \U0001f50d", label_visibility="collapsed")
        with c2:
            if st.form_submit_button("Search", use_container_width=True) and sq:
                st.session_state.q = sq
                st.rerun()

    q = st.session_state.get("q", "")
    if q:
        terms = q.lower().split()
        results = [
            a for a in articles
            if any(
                t in a["headline"].lower()
                or t in a["summary"].lower()
                or t in a["source"].lower()
                or t in a["cat"].lower()
                for t in terms
            )
        ]
        st.html(
            f'<div style="font-size:0.8rem;color:var(--text-tertiary);margin-bottom:1rem;">'
            f'{len(results)} result{"s" if len(results) != 1 else ""} for "{q}"</div>'
        )
        if results:
            render_article_grid(results)
        else:
            st.html(
                f'<div class="glass" style="padding:3rem;text-align:center;color:var(--text-tertiary);font-size:0.9rem;">'
                f'No results for "{q}"</div>'
            )
    render_footer()