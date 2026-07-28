<div align="center">
  <img src="logo.png" alt="SocialPulse Logo" width="64" height="64">
  <h1>SocialPulse — News Hub</h1>
  <p>
    <strong>A real-time news dashboard built with Streamlit.</strong><br>
    Live news across Tech, AI, Business, World, Science, Entertainment & Social Media.
  </p>
  <p>
    <a href="#features">Features</a> •
    <a href="#quick-start">Quick Start</a> •
    <a href="#deployment">Deployment</a> •
    <a href="#tech-stack">Tech Stack</a>
  </p>
  <br>
</div>

---

## Features

- **7 news categories** — Social Media, Tech, World, Business, AI, Science, Entertainment
- **Breaking news ticker** — cycling headlines at the top of the homepage
- **Article detail view** — full article with hero image, author, reading time, bookmark & share
- **Live feed** — auto-refreshing sidebar with simulated breaking alerts
- **Trending topics** — clickable trending page with post counts and volume indicators
- **Full-text search** — search across headlines, summaries, sources and categories
- **Dark theme** — clean, modern dark UI with glassmorphism design
- **Reading progress bar** — scroll-tracking indicator on article pages
- **Keyboard shortcut** — press `/` to focus search from anywhere
- **Responsive** — works on desktop, tablet, and mobile
- **PWA support** — service worker for offline caching

## Quick Start

```bash
# Clone the repo
git clone https://github.com/harman2212/socialpulse-news.git
cd socialpulse-news

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp .env.example .env
# Add your news API key to .env (free at newsdata.io)

# Run the app
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

### API Keys (free)

| Provider | Free Tier | Sign Up |
|---|---|---|
| NewsData.io | 100 requests/day | https://newsdata.io |
| GNews | 100 requests/day | https://gnews.io |
| Mediastack | 500 requests/month | https://mediastack.com |

Add at least one key to `.env` for real news. Without one, the app uses built-in sample articles.

## Testing

```bash
pip install pytest
pytest -v
```

## Deployment

### Streamlit Community Cloud (free)

1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud
3. Click **New app** → select this repo → branch `main` → file `app.py`
4. In Settings → Secrets, add:
   ```toml
   NEWSDATA_API_KEY = "your_key_here"
   SECRET_KEY = "your_secret_key"
   ```

### Docker

```bash
docker compose -f deploy/docker-compose.yml up -d
```

## Project Structure

```
├── app.py                 # Entry point
├── config/                # Settings, categories, article pool
├── data/                  # News API fetcher + fallback data
├── components/            # Nav, cards, UI utilities
├── templates/             # Page templates (home, category, article, etc.)
├── styles/                # CSS (dark theme)
├── db/                    # SQLite database (bookmarks, history, users)
├── deploy/                # Dockerfile, nginx config, docker-compose
├── tests/                 # pytest tests (7 passing)
├── scheduler.py           # Background news refresh
├── logging_setup.py       # Structured logging (loguru)
├── healthz.py             # Health check endpoint
├── sw.js                  # Service worker (PWA)
├── .github/workflows/     # CI/CD pipelines
└── .pre-commit-config.yaml
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit, HTML, CSS, JavaScript |
| Data | NewsData.io / GNews / Mediastack APIs |
| Database | SQLite (SQLAlchemy-style queries) |
| Logging | loguru |
| CI/CD | GitHub Actions |
| Container | Docker + docker-compose |
| Proxy | nginx |

## License

MIT — use it freely.

---

<div align="center">
  <sub>Built with Streamlit • 2026</sub>
</div>