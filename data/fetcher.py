import streamlit as st
import random
import time
from datetime import datetime, timedelta
from config.settings import CATEGORIES, SOURCES, ARTICLE_POOL, LIVE_FEED_TEMPLATES, BREAKING_AUTHORS


@st.cache_data(ttl=600, show_spinner=False)
def get_articles(count=24):
    random.seed(int(time.time()) // 30 * 30)
    now = datetime.now()
    articles, uid = [], 0
    for cat in CATEGORIES:
        pool = ARTICLE_POOL.get(cat, [])
        pool_copy = pool[:]
        random.shuffle(pool_copy)
        for headline, summary in pool_copy[:max(2, count // len(CATEGORIES))]:
            source = random.choice(SOURCES)
            mins_ago = int(random.expovariate(1 / 180)) + 1
            ts = now - timedelta(minutes=mins_ago)
            seed_val = uid * 7 + 13
            img_url = f"https://picsum.photos/seed/{seed_val}/600/400"
            articles.append({
                "id": uid,
                "cat": cat,
                "source": source,
                "headline": headline,
                "summary": summary,
                "body": (
                    f"In the rapidly evolving landscape of digital media, this development marks a significant shift. "
                    f"Industry experts weigh in on the implications for the broader tech landscape. "
                    f"The announcement has generated significant discussion across social media platforms."
                ),
                "time": ts,
                "mins_ago": mins_ago,
                "img_url": img_url,
                "author": random.choice(BREAKING_AUTHORS),
                "read_time": max(1, round(len((headline + " " + summary).split()) / 200)),
                "views": random.randint(1200, 95000),
            })
            uid += 1
    articles.sort(key=lambda x: x["mins_ago"])
    return articles


def get_article_by_id(articles, aid):
    for a in articles:
        if a["id"] == aid:
            return a
    return articles[0] if articles else None


@st.cache_data(ttl=6, show_spinner=False)
def gen_live_feed(count=15):
    now = datetime.now()
    feed = []
    for i in range(count):
        t = LIVE_FEED_TEMPLATES[i % len(LIVE_FEED_TEMPLATES)]
        s = random.choice(t[1])
        tp = random.choice(t[2])
        tp2 = random.choice(["AI", "creator tools", "analytics", "monetization", "safety"])
        p = random.randint(15, 85)
        v = random.randint(1, 30)
        txt = t[0].replace("{s}", s).replace("{p}", str(p)).replace("{v}", str(v)).replace("{t}", tp).replace("{t2}", tp2)
        sc = i * random.randint(20, 150)
        feed.append({
            "text": txt,
            "time": now - timedelta(seconds=sc),
            "color": random.choice(["#6366f1", "#34d399", "#f59e0b", "#ec4899", "#14b8a6"]),
        })
    return feed


def fmt_time_ago(mins):
    if mins < 1:
        return "just now"
    if mins == 1:
        return "1m ago"
    if mins < 60:
        return f"{mins}m ago"
    h, m = divmod(mins, 60)
    if h == 1:
        return f"1h {m}m ago" if m else "1h ago"
    if h < 24:
        return f"{h}h {m}m ago" if m else f"{h}h ago"
    d = h // 24
    return f"{d}d ago" if d < 30 else f"{d // 30}mo ago"