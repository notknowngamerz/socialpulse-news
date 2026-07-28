<div align="center">
  <img src="logo.png" alt="SocialPulse Logo" width="64" height="64">
  <h1>SocialPulse — News Hub</h1>
  <p>
    <strong>A news dashboard built with Streamlit.</strong><br>
    7 categories, 180+ articles, dark glassmorphism UI.<br><br>
    <a href="https://socialpulse-news.streamlit.app/" target="_blank"><strong>Live Demo →</strong></a>
  </p>
  <p>
    <a href="#features">Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#deploy">Deploy</a>
  </p>
  <br>
</div>

---

## Features

- **7 news categories** — Social Media, Tech, World, Business, AI, Science, Entertainment
- **180+ articles** — built-in sample pool, no API key required
- **Breaking news ticker** — cycling headlines on the homepage
- **Article detail view** — hero image, author, read time, bookmark & share
- **Live feed** — auto-refreshing simulated breaking alerts
- **Trending topics** — post counts and volume indicators
- **Full-text search** — across headlines, summaries, sources and categories
- **Dark glassmorphism UI** — responsive on desktop, tablet, and mobile
- **Reading progress bar** — scroll-tracker on article pages
- **Keyboard shortcut** — press `/` to focus search
- **PWA** — service worker for offline caching

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in your browser. No configuration needed.

## Deploy

Push to GitHub and deploy on any of these for free:

| Platform | How |
|---|---|
| **Streamlit Cloud** | streamlit.io/cloud → New app → select repo → `app.py` |
| **Hugging Face Spaces** | huggingface.co → New Space → SDK: Streamlit → connect repo |
| **Render** | render.com → New Web Service → start command: `streamlit run app.py --server.port 10000` |

## Testing

```bash
pip install pytest
pytest -v
```

## Project Structure

```
├── app.py                 # Entry point
├── config/settings.py     # Categories, article pool, constants
├── data/fetcher.py        # Article generator + helpers
├── components/            # Nav, cards, UI utilities
├── templates/             # Page templates
├── styles/                # CSS (dark theme)
├── tests/                 # pytest (4 passing)
├── deploy/                # Docker support
├── sw.js                  # Service worker (PWA)
└── .github/workflows/     # CI
```

## License

MIT — use it freely.

---

<div align="center">
  <sub>Built with Streamlit • 2026</sub>
</div>