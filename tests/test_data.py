import pytest
from datetime import datetime, timedelta
from data.fetcher import fmt_time_ago, gen_live_feed


def test_fmt_time_ago():
    assert fmt_time_ago(0) == "just now"
    assert fmt_time_ago(1) == "1m ago"
    assert fmt_time_ago(30) == "30m ago"
    assert fmt_time_ago(60) == "1h ago"
    assert fmt_time_ago(90) == "1h 30m ago"
    assert fmt_time_ago(150) == "2h 30m ago"
    assert fmt_time_ago(1440) == "1d ago"
    assert fmt_time_ago(2880) == "2d ago"


def test_live_feed():
    feed = gen_live_feed(10)
    assert len(feed) == 10
    for item in feed:
        assert "text" in item
        assert "time" in item
        assert "color" in item


def test_fallback_articles():
    from data.fetcher import get_articles
    arts = get_articles(21)
    assert len(arts) == 21
    for a in arts:
        assert "id" in a
        assert "headline" in a
        assert "cat" in a
        assert "source" in a


def test_fallback_articles_all_categories_represented():
    from data.fetcher import get_articles
    from config.settings import CATEGORIES
    arts = get_articles(28)
    cats_in_result = set(a["cat"] for a in arts)
    for cat in CATEGORIES:
        assert cat in cats_in_result, f"missing category: {cat}"