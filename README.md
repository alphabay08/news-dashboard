# 🌍 Global News Dashboard — Backend v2.0

A personal always-on news terminal. Fetches top 10 articles hourly from **90+ RSS feeds** across **11 categories** with concurrent async fetching.

---

## 📁 Project Structure

```
news-backend/
├── app/
│   ├── main.py          # FastAPI app, all API routes
│   ├── fetcher.py       # Async concurrent RSS fetcher + OG image extractor
│   ├── store.py         # In-memory store: search, bookmarks, read tracking
│   └── scheduler.py     # APScheduler: hourly refresh + keep-alive
├── feeds/
│   └── registry.py      # 90+ RSS feeds across 11 categories
├── requirements.txt
├── render.yaml          # Render.com deployment config
├── run.py               # Local dev entry point
└── .env.example
```

---

## 🚀 Local Development

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python run.py
# or: uvicorn app.main:app --reload
```

Open http://localhost:8000/docs for interactive API explorer.

---

## 📡 API Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/status` | GET | Stats: article count, feeds OK/failed, last refresh |
| `/api/categories` | GET | Full category tree with counts |
| `/api/articles` | GET | Articles (filter by category/subcategory, paginate) |
| `/api/articles/{id}` | GET | Single article by ID |
| `/api/search?q=...` | GET | Full-text search across all articles |
| `/api/bookmarks` | GET | All bookmarked articles |
| `/api/bookmarks/{id}` | POST | Toggle bookmark |
| `/api/read/{id}` | POST | Mark article as read |
| `/api/read/{id}` | DELETE | Mark article as unread |
| `/api/trending` | GET | Trending keywords across all titles |
| `/api/feeds/health` | GET | Per-feed status (ok/timeout/error) |
| `/api/feeds/registry` | GET | All registered feeds |
| `/api/refresh` | POST | Trigger manual refresh |

### Query Parameters — `/api/articles`
- `category` — e.g. `world`, `pakistan`, `sports`, `showbiz`
- `subcategory` — e.g. `cricket`, `football`, `hollywood`, `bollywood`
- `limit` — default 50, max 200
- `offset` — for pagination
- `sort_by` — `date` (default) or `source`

---

## 🌐 Hosting — R&D Findings & Recommendations

### Problem: Render Free Tier Sleeps
Render's free tier spins down after 15 min of inactivity. UptimeRobot pings don't reliably prevent this.

### ✅ Best Free/Near-Free Hosting Options (2024)

| Platform | Free Tier | Always-On | Notes |
|----------|-----------|-----------|-------|
| **Koyeb** | ✅ 1 free service | ✅ Yes | Best free always-on. Nano instance, 512MB RAM |
| **Railway** | ✅ $5/mo credit | ✅ Yes | Most generous. ~500 hrs/mo free. Best DX |
| **Fly.io** | ✅ 3 shared VMs | ✅ Yes | 256MB RAM free. `fly launch` is easy |
| **Render** | ✅ Free web service | ❌ Sleeps | Needs paid plan ($7/mo) for always-on |
| **Cyclic.sh** | ✅ Free | ✅ Yes | Node-first, Python experimental |

### 🏆 Recommendation: **Railway** (easiest) or **Koyeb** (truly free)

**Railway Setup:**
```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

**Koyeb Setup:**
1. Push to GitHub
2. Connect repo on koyeb.com
3. Set build: `pip install -r requirements.txt`
4. Set run: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

---

## 🖼️ Article Images — R&D Findings

### Problem: Most RSS feeds don't include images

### Solutions Implemented (in priority order):

1. **`media:content` / `media:thumbnail`** — parsed from RSS entries (works for BBC, Reuters, Al Jazeera)
2. **`<enclosure>` tags** — image attachments in RSS
3. **HTML parsing of `<summary>`** — extracts `<img>` tags from RSS description HTML
4. **Open Graph scraping** — fetches article URL and extracts `og:image` meta tag

The OG scraping is optional (slower) — enable via `/api/refresh?fetch_images=true` or set `fetch_images=True` in scheduler.

### Success rates by feed type:
- Major outlets (BBC, Reuters, Guardian): ~80% have images in RSS
- Pakistani news (Dawn, Geo, ARY): ~40-60% via OG fallback
- Pure-text feeds (Hacker News, EurekAlert): 0% — use category placeholder

---

## 🔍 Full-Text Search

Built-in search via `/api/search?q=imran+khan&category=pakistan`

**Algorithm:** TF-style scoring — counts term occurrences in title + summary, ranks by score.

**Upgrade path:** For production-grade search, add **Meilisearch** (free self-hosted) or **Typesense Cloud** (free tier: 100k docs).

---

## 💾 Database — Should You Add One?

### Current: In-memory (resets on restart)

### When to add SQLite:
- You want bookmarks/read status to survive server restarts
- You want article history across multiple refreshes
- You want to run the feed parser less frequently

### SQLite upgrade (simple):
```python
# pip install aiosqlite
import aiosqlite
# Store articles in articles table, bookmarks in bookmarks table
# Upsert on article_id to avoid duplicates
```

**Recommendation for now:** Keep in-memory. It's simpler and restarts are rare on Railway/Koyeb. Add SQLite when bookmarks persistence becomes important.

---

## 🩺 Dead Feed Detection

The fetcher automatically:
- Times out feeds that don't respond in 15 seconds
- Records HTTP status codes (404, 403, 500, etc.)
- Marks feeds as `timeout`, `error`, or `ok`
- `/api/feeds/health` shows which feeds are broken

**Replacement feeds for known broken ones:**
- Samaa TV → `https://www.samaaenglish.tv/feed/` 
- Arab News → `https://www.arabnews.com/rss.xml` ✅ (already in registry)
- Gulf News → `https://gulfnews.com/rss` 
- Korea Herald → `https://www.koreaherald.com/rss/rss_all.php`
- USA Today → `https://rssfeeds.usatoday.com/usatoday-NewsTopStories`

---

## ⚡ Concurrent Fetching

All 90+ feeds are fetched in parallel using `asyncio` + `aiohttp`:
- Max 50 concurrent connections
- Max 2 connections per host (polite)
- 15s total timeout, 8s connect timeout
- ~8-12 seconds total for all 90 feeds (vs ~15 minutes sequential)

---

## 🔮 Future Improvements (Roadmap)

### Phase 2 — Frontend
- [ ] React + Vite frontend (replace single HTML)
- [ ] Dark/light mode toggle
- [ ] Mobile-responsive layout
- [ ] Keyboard shortcuts

### Phase 3 — Intelligence
- [ ] AI summarization via Claude API (free via claude.ai is not an API, use Groq free tier with Llama)
- [ ] Trending topic detection ✅ (basic version done)
- [ ] Language detection + multi-language feeds (Arabic, Urdu)
- [ ] Duplicate article detection (cosine similarity on titles)

### Phase 4 — Scale
- [ ] SQLite persistence for bookmarks
- [ ] Redis caching (Upstash free tier: 10k req/day)
- [ ] WebSocket push for live updates
- [ ] Export bookmarks as PDF/email digest

---

## 📰 Additional Feed Recommendations

### Pakistan
- Samaa English: `https://www.samaaenglish.tv/feed/`
- Hum News: `https://www.humnews.pk/feed/`
- Geo Urdu: `https://urdu.geo.tv/rss/1/`
- Daily Jang (Urdu): `https://jang.com.pk/rss/1.xml`

### Sports  
- Cricbuzz Pakistan: `https://www.cricbuzz.com/cricket-rss-feeds/feed.rss`
- Supersport: `https://www.supersport.com/rss/news`
- Sportstar Cricket: `https://sportstar.thehindu.com/cricket/?service=rss`

### Showbiz
- Something Hollywood: `https://www.somethingholly.com/feed/`
- Lollywood news: `https://www.brandsynario.com/feed/`
- Reviewit.pk: `https://reviewit.pk/feed/`
