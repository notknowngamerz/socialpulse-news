import streamlit as st
from datetime import datetime
from data.fetcher import fmt_time_ago
from config.settings import CAT_COLORS, BREAKING_HEADS, BREAKING_SUMMARIES, BREAKING_SOURCES, BREAKING_AUTHORS


def _build_card_html(art):
    ts = fmt_time_ago(art["mins_ago"])
    tc = CAT_COLORS.get(art["cat"], "#a78bfa")
    is_new = art["mins_ago"] < 30
    is_hot = art["views"] > 40000
    status = ""
    if is_new:
        status = '<span class="status-new">\u25cf New</span>'
    elif is_hot:
        status = '<span class="status-hot">\u25cf Hot</span>'
    a = art
    return (
        f'<a href="?page=article&id={a["id"]}" target="_self" style="text-decoration:none;display:block;height:100%;">'
        f'<div class="article-card" style="border-color:{tc}18;">'
        f'<div class="article-img" style="background-image:url(\'{a["img_url"]}\');">'
        f'<span class="img-source">{a["source"]}</span>'
        f'<span class="img-tag" style="background:{tc}22;color:{tc};border-color:{tc}33;">{a["cat"]}</span>'
        f'</div>'
        f'<div class="article-body">'
        f'<div class="cat" style="color:{tc};">{a["cat"]}</div>'
        f'<div class="title">{a["headline"]}</div>'
        f'<div class="desc">{a["summary"]}</div>'
        f'<div class="meta">'
        f'<div class="left">'
        f'<span class="source">{a["source"]}</span>'
        f'<span class="read-time">\u00b7 {a["read_time"]} min</span>'
        f'</div>'
        f'<div class="right">{status}'
        f'<span class="view-count">{a["views"] // 1000}K</span>'
        f'<span>{ts}</span>'
        f'</div>'
        f'</div>'
        f'</div>'
        f'</div>'
        f'</a>'
    )


def render_article_grid(articles, cols=3):
    cards_html = "".join(_build_card_html(art) for art in articles)
    st.html(f'<div class="article-grid" style="--cols:{cols};">{cards_html}</div>')


def render_section_header(title, link="#"):
    st.html(
        '<div class="section-header"><h2>' + title + '</h2>'
        '<a href="' + link + '" target="_self" style="text-decoration:none;">'
        '<span class="see-all">See all \u2192</span></a></div>'
    )


def render_breaking(bi):
    bs, ba = BREAKING_SOURCES, BREAKING_AUTHORS
    st.html(
        '<a href="?page=article&id=' + str(bi) + '" target="_self" style="text-decoration:none;display:block;">'
        '<div class="breaking-wrap">'
        '<div class="breaking-label">\u26a1 Breaking</div>'
        '<div class="breaking-title">' + BREAKING_HEADS[bi] + '</div>'
        '<div style="font-size:0.85rem;color:rgba(255,255,255,0.55);margin-bottom:0.6rem;line-height:1.6;">' + BREAKING_SUMMARIES[bi] + '</div>'
        '<div class="breaking-meta">'
        '<span class="src">' + bs[bi % len(bs)] + '</span><span>\u00b7</span><span>' + ba[bi % len(ba)] + '</span>'
        '<span>\u00b7</span><span>' + datetime.now().strftime("%b %d, %Y") + ' ' + datetime.now().strftime("%I:%M %p") + '</span>'
        '</div>'
        '</div>'
        '</a>'
    )