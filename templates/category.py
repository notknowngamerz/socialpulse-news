import streamlit as st
from components.nav import render_nav
from components.cards import render_article_grid
from components.ui import render_footer
from config.settings import CAT_ICONS


def page_category(articles, cat_name):
    render_nav("category", cat_name)
    icon_all = chr(0x1f4f0)
    if cat_name == "All":
        filtered, prefix = articles, f"{icon_all} All News"
    else:
        filtered = [a for a in articles if a["cat"] == cat_name]
        icon = CAT_ICONS.get(cat_name, icon_all)
        prefix = f"{icon} {cat_name}"
    st.html(
        f'<div class="section-header"><h2>{prefix} '
        f'<span style="font-size:0.8rem;color:var(--text-tertiary);font-weight:400;">({len(filtered)})</span></h2></div>'
    )
    if filtered:
        render_article_grid(filtered)
    else:
        st.html(
            '<div class="glass" style="padding:3rem;text-align:center;color:var(--text-tertiary);font-size:0.9rem;">'
            'No articles found.</div>'
        )
    render_footer()