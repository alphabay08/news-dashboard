# app/main.py
"""
Global News Dashboard — FastAPI Backend
Features:
- Concurrent RSS fetching (90+ feeds)
- Category/subcategory browsing
- Full-text search
- Bookmarks & read tracking
- Trending topics
- Feed health dashboard
- CORS enabled for Netlify frontend
"""

import asyncio
import logging
import os
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Optional

import httpx
import pytz
from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.fetcher import fetch_all_feeds
from app.store import store
from app.scheduler import setup_scheduler, scheduler
from feeds.registry import FEEDS, get_all_feeds_flat

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
PKT = pytz.timezone("Asia/Karachi")

ALL_FEEDS = get_all_feeds_flat()
is_refreshing = False


async def do_refresh(fetch_images: bool = False):
    """Main refresh logic: fetch all feeds and ingest into store."""
    global is_refreshing
    if is_refreshing:
        logger.info("Refresh already in progress, skipping.")
        return
    is_refreshing = True
    try:
        logger.info("Fetching %d feeds concurrently...", len(ALL_FEEDS))
        results = await fetch_all_feeds(ALL_FEEDS, fetch_images=fetch_images)
        store.ingest(results)
        next_refresh = datetime.now(PKT) + timedelta(hours=1)
        store.set_next_refresh(next_refresh)
        stats = store.get_stats()
        logger.info(
            "Refresh complete: %d articles, %d/%d feeds OK",
            stats["total_articles"],
            stats["successful_feeds"],
            stats["total_feeds"],
        )
    finally:
        is_refreshing = False


async def self_ping():
    """Keep-alive self-ping."""
    base_url = os.environ.get("RENDER_EXTERNAL_URL", "http://localhost:8000")
    try:
        async with httpx.AsyncClient() as client:
            await client.get(f"{base_url}/health", timeout=10)
            logger.debug("Self-ping OK")
    except Exception as e:
        logger.debug("Self-ping failed: %s", e)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: initial feed fetch + scheduler."""
    logger.info("=== News Dashboard Backend Starting ===")
    logger.info("Loaded %d feeds across %d categories", len(ALL_FEEDS), len(FEEDS))

    # Initial fetch on startup
    await do_refresh()

    # Setup hourly scheduler
    setup_scheduler(do_refresh, self_ping)

    yield

    # Shutdown
    scheduler.shutdown(wait=False)
    logger.info("=== News Dashboard Backend Stopped ===")


app = FastAPI(
    title="Global News Dashboard API",
    description="Personal news aggregator with 90+ RSS feeds across 11 categories.",
    version="2.0.0",
    lifespan=lifespan,
)

# CORS — allow Netlify + localhost dev
ALLOWED_ORIGINS = [
    "https://*.netlify.app",
    "https://*.netlify.com",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8080",
    "*",  # Open for personal use — restrict in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Health & Status ──────────────────────────────────────────────────────────

@app.get("/health", tags=["Status"])
async def health():
    return {"status": "ok", "time_pkt": datetime.now(PKT).strftime("%d %b %Y %I:%M %p PKT")}


@app.get("/api/status", tags=["Status"])
async def status():
    return {
        "ok": True,
        "is_refreshing": is_refreshing,
        **store.get_stats(),
    }


# ─── Categories ───────────────────────────────────────────────────────────────

@app.get("/api/categories", tags=["Categories"])
async def get_categories():
    """Return full category + subcategory tree with article counts."""
    stats = store.get_stats()
    cat_counts = stats["articles_by_category"]
    result = []
    for cat_key, cat in FEEDS.items():
        item = {
            "key": cat_key,
            "label": cat["label"],
            "icon": cat["icon"],
            "article_count": cat_counts.get(cat_key, 0),
            "subcategories": None,
        }
        if cat.get("subcategories"):
            subs = []
            for sub_key, sub in cat["subcategories"].items():
                feed_names = [f["name"] for f in sub["feeds"]]
                subs.append({
                    "key": sub_key,
                    "label": sub["label"],
                    "icon": sub["icon"],
                    "feeds": feed_names,
                })
            item["subcategories"] = subs
        result.append(item)
    return result


# ─── Articles ─────────────────────────────────────────────────────────────────

@app.get("/api/articles", tags=["Articles"])
async def get_articles(
    category: Optional[str] = Query(None, description="Category key e.g. 'world'"),
    subcategory: Optional[str] = Query(None, description="Subcategory key e.g. 'cricket'"),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    sort_by: str = Query("date", regex="^(date|source)$"),
):
    if category and category not in FEEDS:
        raise HTTPException(status_code=404, detail=f"Category '{category}' not found")

    result = store.get_articles(
        category=category,
        subcategory=subcategory,
        limit=limit,
        offset=offset,
        sort_by=sort_by,
    )
    return result


@app.get("/api/articles/{article_id}", tags=["Articles"])
async def get_article(article_id: str):
    article = store.get_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


# ─── Search ───────────────────────────────────────────────────────────────────

@app.get("/api/search", tags=["Search"])
async def search_articles(
    q: str = Query(..., min_length=2, max_length=100, description="Search query"),
    category: Optional[str] = Query(None),
    limit: int = Query(30, ge=1, le=100),
):
    results = store.search(query=q, category=category, limit=limit)
    return {"query": q, "count": len(results), "articles": results}


# ─── Read / Bookmarks ─────────────────────────────────────────────────────────

class ArticleAction(BaseModel):
    article_id: str


@app.post("/api/read/{article_id}", tags=["User"])
async def mark_read(article_id: str):
    store.mark_read(article_id)
    return {"ok": True, "article_id": article_id, "action": "read"}


@app.delete("/api/read/{article_id}", tags=["User"])
async def mark_unread(article_id: str):
    store.mark_unread(article_id)
    return {"ok": True, "article_id": article_id, "action": "unread"}


@app.post("/api/bookmarks/{article_id}", tags=["User"])
async def toggle_bookmark(article_id: str):
    is_bookmarked = store.toggle_bookmark(article_id)
    return {"ok": True, "article_id": article_id, "is_bookmarked": is_bookmarked}


@app.get("/api/bookmarks", tags=["User"])
async def get_bookmarks():
    articles = store.get_bookmarks()
    return {"count": len(articles), "articles": articles}


# ─── Trending ─────────────────────────────────────────────────────────────────

@app.get("/api/trending", tags=["Discovery"])
async def get_trending(top_n: int = Query(15, ge=5, le=50)):
    return {"trending": store.get_trending(top_n=top_n)}


# ─── Feed Health ──────────────────────────────────────────────────────────────

@app.get("/api/feeds/health", tags=["Admin"])
async def feed_health():
    feeds = store.get_feed_health()
    total = len(feeds)
    ok = sum(1 for f in feeds if f["status"] == "ok")
    return {
        "summary": {"total": total, "ok": ok, "failed": total - ok},
        "feeds": feeds,
    }


@app.get("/api/feeds/registry", tags=["Admin"])
async def feed_registry():
    """Return the full feed registry."""
    return {"feeds": ALL_FEEDS, "total": len(ALL_FEEDS)}


# ─── Manual Refresh ───────────────────────────────────────────────────────────

@app.post("/api/refresh", tags=["Admin"])
async def manual_refresh(
    background_tasks: BackgroundTasks,
    fetch_images: bool = Query(False, description="Also fetch OG images (slower)"),
):
    if is_refreshing:
        return {"ok": False, "message": "Refresh already in progress"}
    background_tasks.add_task(do_refresh, fetch_images)
    return {"ok": True, "message": "Refresh started in background"}


# ─── Root ─────────────────────────────────────────────────────────────────────

@app.get("/", tags=["Status"])
async def root():
    stats = store.get_stats()
    return {
        "service": "Global News Dashboard API",
        "version": "2.0.0",
        "docs": "/docs",
        "status": "running",
        "articles": stats["total_articles"],
        "last_refresh": stats["last_refresh_human"],
    }
