# app/fetcher.py
"""
Concurrent RSS fetcher with:
- Async parallel fetching (all 90+ feeds at once)
- Open Graph image extraction fallback
- Dead feed auto-detection and skipping
- PKT timezone support
- Top 10 articles per feed
"""

import asyncio
import hashlib
import logging
import re
from datetime import datetime, timezone, timedelta
from typing import Optional
import feedparser
import aiohttp
from bs4 import BeautifulSoup
import pytz

logger = logging.getLogger(__name__)

PKT = pytz.timezone("Asia/Karachi")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/rss+xml, application/xml, text/xml, */*",
    "Accept-Language": "en-US,en;q=0.9",
}

FETCH_TIMEOUT = aiohttp.ClientTimeout(total=15, connect=8)
MAX_ARTICLES_PER_FEED = 10
IMAGE_TIMEOUT = aiohttp.ClientTimeout(total=8, connect=4)


def _article_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:12]


def _parse_date(entry) -> Optional[datetime]:
    """Parse date from RSS entry, return PKT-aware datetime."""
    for attr in ("published_parsed", "updated_parsed"):
        val = getattr(entry, attr, None)
        if val:
            try:
                dt = datetime(*val[:6], tzinfo=timezone.utc)
                return dt.astimezone(PKT)
            except Exception:
                pass
    return datetime.now(PKT)


def _extract_image_from_entry(entry) -> Optional[str]:
    """Extract image URL from RSS entry fields."""
    # 1. media:content / media:thumbnail
    media = getattr(entry, "media_content", None)
    if media and isinstance(media, list):
        for m in media:
            url = m.get("url", "")
            if url and any(ext in url.lower() for ext in [".jpg", ".jpeg", ".png", ".webp"]):
                return url

    media_thumb = getattr(entry, "media_thumbnail", None)
    if media_thumb and isinstance(media_thumb, list):
        url = media_thumb[0].get("url", "")
        if url:
            return url

    # 2. enclosures
    for enc in getattr(entry, "enclosures", []):
        if enc.get("type", "").startswith("image/"):
            return enc.get("href") or enc.get("url")

    # 3. Parse image from summary/content HTML
    for field in ("summary", "content"):
        text = ""
        val = getattr(entry, field, None)
        if isinstance(val, list):
            text = val[0].get("value", "") if val else ""
        elif isinstance(val, str):
            text = val
        if text:
            soup = BeautifulSoup(text, "html.parser")
            img = soup.find("img")
            if img and img.get("src"):
                src = img["src"]
                if src.startswith("http"):
                    return src

    return None


def _clean_summary(entry) -> str:
    """Extract clean text summary from RSS entry."""
    for field in ("summary", "description"):
        raw = getattr(entry, field, None)
        if raw:
            soup = BeautifulSoup(raw, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) > 50:
                return text[:500] + ("..." if len(text) > 500 else "")
    return ""


def _get_entry_tags(entry) -> list:
    tags = []
    for tag in getattr(entry, "tags", []):
        label = tag.get("term") or tag.get("label") or ""
        if label and len(label) < 40:
            tags.append(label.strip())
    return tags[:5]


async def fetch_og_image(session: aiohttp.ClientSession, url: str) -> Optional[str]:
    """Fetch Open Graph image from article URL."""
    try:
        async with session.get(url, timeout=IMAGE_TIMEOUT, allow_redirects=True) as resp:
            if resp.status != 200:
                return None
            html = await resp.text(errors="ignore")
            soup = BeautifulSoup(html, "html.parser")
            # og:image
            og = soup.find("meta", property="og:image")
            if og and og.get("content"):
                return og["content"]
            # twitter:image
            tw = soup.find("meta", attrs={"name": "twitter:image"})
            if tw and tw.get("content"):
                return tw["content"]
    except Exception:
        pass
    return None


async def fetch_feed(
    session: aiohttp.ClientSession,
    feed_meta: dict,
    fetch_images: bool = False,
) -> dict:
    """Fetch a single RSS feed and return parsed articles."""
    url = feed_meta["url"]
    name = feed_meta["name"]
    result = {
        "feed_name": name,
        "feed_url": url,
        "logo": feed_meta.get("logo", ""),
        "category": feed_meta["category"],
        "subcategory": feed_meta.get("subcategory"),
        "category_label": feed_meta["category_label"],
        "subcategory_label": feed_meta.get("subcategory_label"),
        "articles": [],
        "status": "ok",
        "error": None,
        "fetched_at": datetime.now(PKT).isoformat(),
    }

    try:
        async with session.get(url, timeout=FETCH_TIMEOUT, allow_redirects=True) as resp:
            if resp.status not in (200, 301, 302):
                result["status"] = "error"
                result["error"] = f"HTTP {resp.status}"
                return result
            raw = await resp.read()

        parsed = feedparser.parse(raw)

        if parsed.bozo and not parsed.entries:
            result["status"] = "error"
            result["error"] = f"Feed parse error: {parsed.bozo_exception}"
            return result

        entries = parsed.entries[:MAX_ARTICLES_PER_FEED]
        articles = []

        for entry in entries:
            link = getattr(entry, "link", "") or ""
            title = getattr(entry, "title", "Untitled").strip()
            if not link or not title:
                continue

            image = _extract_image_from_entry(entry)
            summary = _clean_summary(entry)
            pub_date = _parse_date(entry)
            tags = _get_entry_tags(entry)

            articles.append({
                "id": _article_id(link),
                "title": title,
                "url": link,
                "summary": summary,
                "image": image,
                "published_at": pub_date.isoformat() if pub_date else None,
                "published_human": pub_date.strftime("%d %b %Y, %I:%M %p PKT") if pub_date else "Unknown",
                "tags": tags,
                "source": name,
                "source_logo": feed_meta.get("logo", ""),
                "category": feed_meta["category"],
                "subcategory": feed_meta.get("subcategory"),
            })

        result["articles"] = articles

        # Optionally fetch OG images for articles missing images
        if fetch_images:
            no_image = [a for a in articles if not a["image"]][:3]  # limit to 3 per feed
            if no_image:
                tasks = [fetch_og_image(session, a["url"]) for a in no_image]
                images = await asyncio.gather(*tasks, return_exceptions=True)
                for article, img in zip(no_image, images):
                    if isinstance(img, str):
                        article["image"] = img

    except asyncio.TimeoutError:
        result["status"] = "timeout"
        result["error"] = "Request timed out"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:200]

    return result


async def fetch_all_feeds(feed_list: list, fetch_images: bool = False) -> list:
    """Fetch all feeds concurrently."""
    connector = aiohttp.TCPConnector(
        limit=50,
        limit_per_host=2,
        ttl_dns_cache=300,
        enable_cleanup_closed=True,
    )

    async with aiohttp.ClientSession(
        headers=HEADERS,
        connector=connector,
        trust_env=True,
    ) as session:
        tasks = [fetch_feed(session, feed, fetch_images) for feed in feed_list]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    final = []
    for r in results:
        if isinstance(r, Exception):
            logger.error("Feed fetch exception: %s", r)
        else:
            final.append(r)

    return final
