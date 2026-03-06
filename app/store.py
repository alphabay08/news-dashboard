# app/store.py
"""
In-memory article store with:
- Per-category/subcategory indexing
- Full-text search
- Read/unread tracking (session-based)
- Bookmarks (session-based)
- Feed health tracking
- Trending topics extraction
"""

import re
import logging
from collections import defaultdict, Counter
from datetime import datetime
from typing import Optional
import pytz

logger = logging.getLogger(__name__)
PKT = pytz.timezone("Asia/Karachi")

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "has", "have",
    "had", "be", "been", "being", "that", "this", "these", "those", "it",
    "its", "as", "after", "before", "during", "over", "under", "about",
    "into", "through", "between", "against", "report", "says", "said",
    "new", "will", "can", "get", "also", "more", "out", "up", "than",
    "would", "could", "should", "what", "which", "when", "where", "how",
}


class NewsStore:
    def __init__(self):
        self._articles: dict = {}           # id -> article
        self._by_category: dict = defaultdict(list)    # category -> [ids]
        self._by_subcategory: dict = defaultdict(list)  # (cat, subcat) -> [ids]
        self._feed_stats: dict = {}         # feed_url -> {status, count, error, fetched_at}
        self._last_refresh: Optional[datetime] = None
        self._next_refresh: Optional[datetime] = None
        self._bookmarks: set = set()        # article ids
        self._read: set = set()             # article ids
        self._total_feeds: int = 0
        self._successful_feeds: int = 0

    def ingest(self, feed_results: list):
        """Ingest fresh feed results, replacing old data."""
        new_articles = {}
        new_by_cat = defaultdict(list)
        new_by_subcat = defaultdict(list)
        feed_stats = {}
        successful = 0

        for feed_result in feed_results:
            feed_url = feed_result["feed_url"]
            status = feed_result["status"]
            articles = feed_result.get("articles", [])

            feed_stats[feed_url] = {
                "name": feed_result["feed_name"],
                "status": status,
                "article_count": len(articles),
                "error": feed_result.get("error"),
                "fetched_at": feed_result.get("fetched_at"),
                "logo": feed_result.get("logo", ""),
                "category": feed_result.get("category"),
                "subcategory": feed_result.get("subcategory"),
            }

            if status == "ok" and articles:
                successful += 1

            for article in articles:
                aid = article["id"]
                new_articles[aid] = article
                cat = article["category"]
                subcat = article.get("subcategory")
                new_by_cat[cat].append(aid)
                if subcat:
                    new_by_subcat[(cat, subcat)].append(aid)

        # Preserve bookmarks and read status
        self._articles = new_articles
        self._by_category = new_by_cat
        self._by_subcategory = new_by_subcat
        self._feed_stats = feed_stats
        self._last_refresh = datetime.now(PKT)
        self._successful_feeds = successful
        self._total_feeds = len(feed_results)

        logger.info(
            "Store ingested: %d articles from %d/%d feeds",
            len(new_articles), successful, len(feed_results)
        )

    def set_next_refresh(self, dt: datetime):
        self._next_refresh = dt

    def get_articles(
        self,
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        sort_by: str = "date",
    ) -> dict:
        if category:
            if subcategory:
                ids = self._by_subcategory.get((category, subcategory), [])
            else:
                ids = self._by_category.get(category, [])
        else:
            ids = list(self._articles.keys())

        articles = [self._articles[i] for i in ids if i in self._articles]

        # Sort
        if sort_by == "date":
            articles.sort(
                key=lambda a: a.get("published_at") or "",
                reverse=True,
            )

        total = len(articles)
        paginated = articles[offset: offset + limit]

        # Annotate with read/bookmark status
        for a in paginated:
            a["is_read"] = a["id"] in self._read
            a["is_bookmarked"] = a["id"] in self._bookmarks

        return {"articles": paginated, "total": total, "offset": offset, "limit": limit}

    def search(self, query: str, category: Optional[str] = None, limit: int = 50) -> list:
        """Simple full-text search across title + summary."""
        if not query or len(query.strip()) < 2:
            return []

        terms = [t.lower() for t in re.split(r"\s+", query.strip()) if t]

        if category:
            ids = self._by_category.get(category, [])
            candidates = [self._articles[i] for i in ids if i in self._articles]
        else:
            candidates = list(self._articles.values())

        results = []
        for article in candidates:
            text = (article.get("title", "") + " " + article.get("summary", "")).lower()
            score = sum(text.count(term) for term in terms)
            if score > 0:
                results.append((score, article))

        results.sort(key=lambda x: x[0], reverse=True)
        out = [a for _, a in results[:limit]]

        for a in out:
            a["is_read"] = a["id"] in self._read
            a["is_bookmarked"] = a["id"] in self._bookmarks

        return out

    def get_article(self, article_id: str) -> Optional[dict]:
        a = self._articles.get(article_id)
        if a:
            a["is_read"] = article_id in self._read
            a["is_bookmarked"] = article_id in self._bookmarks
        return a

    def mark_read(self, article_id: str):
        if article_id in self._articles:
            self._read.add(article_id)

    def mark_unread(self, article_id: str):
        self._read.discard(article_id)

    def toggle_bookmark(self, article_id: str) -> bool:
        if article_id in self._bookmarks:
            self._bookmarks.discard(article_id)
            return False
        else:
            self._bookmarks.add(article_id)
            return True

    def get_bookmarks(self) -> list:
        out = []
        for aid in self._bookmarks:
            a = self._articles.get(aid)
            if a:
                a = dict(a)
                a["is_read"] = aid in self._read
                a["is_bookmarked"] = True
                out.append(a)
        out.sort(key=lambda a: a.get("published_at") or "", reverse=True)
        return out

    def get_trending(self, top_n: int = 10) -> list:
        """Extract trending keywords across all article titles."""
        word_counter = Counter()
        for article in self._articles.values():
            title = article.get("title", "")
            words = re.findall(r"\b[a-zA-Z]{3,}\b", title)
            for w in words:
                w_lower = w.lower()
                if w_lower not in STOP_WORDS and len(w_lower) > 3:
                    word_counter[w] += 1

        return [{"word": w, "count": c} for w, c in word_counter.most_common(top_n)]

    def get_stats(self) -> dict:
        cat_counts = {}
        for cat, ids in self._by_category.items():
            cat_counts[cat] = len([i for i in ids if i in self._articles])

        return {
            "total_articles": len(self._articles),
            "total_feeds": self._total_feeds,
            "successful_feeds": self._successful_feeds,
            "failed_feeds": self._total_feeds - self._successful_feeds,
            "bookmarks_count": len(self._bookmarks),
            "read_count": len(self._read),
            "last_refresh": self._last_refresh.isoformat() if self._last_refresh else None,
            "last_refresh_human": self._last_refresh.strftime("%d %b %Y, %I:%M %p PKT") if self._last_refresh else "Never",
            "next_refresh": self._next_refresh.isoformat() if self._next_refresh else None,
            "articles_by_category": cat_counts,
        }

    def get_feed_health(self) -> list:
        feeds = []
        for url, stat in self._feed_stats.items():
            feeds.append({
                "name": stat["name"],
                "url": url,
                "status": stat["status"],
                "article_count": stat["article_count"],
                "error": stat["error"],
                "fetched_at": stat["fetched_at"],
                "logo": stat["logo"],
                "category": stat["category"],
                "subcategory": stat["subcategory"],
            })
        feeds.sort(key=lambda f: (f["status"] != "ok", f["name"]))
        return feeds


# Global singleton store
store = NewsStore()
