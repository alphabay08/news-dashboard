# app/scheduler.py
"""
APScheduler with hourly refresh + self-ping keep-alive.
"""

import asyncio
import logging
from datetime import datetime, timedelta
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

logger = logging.getLogger(__name__)
PKT = pytz.timezone("Asia/Karachi")

scheduler = AsyncIOScheduler(timezone=PKT)


def setup_scheduler(refresh_func, self_ping_func=None):
    """Configure and start the scheduler."""

    async def hourly_refresh():
        logger.info("[Scheduler] Starting hourly RSS refresh...")
        try:
            await refresh_func()
        except Exception as e:
            logger.error("[Scheduler] Refresh error: %s", e)

    scheduler.add_job(
        hourly_refresh,
        trigger=IntervalTrigger(hours=1, timezone=PKT),
        id="hourly_refresh",
        name="Hourly RSS Refresh",
        replace_existing=True,
        max_instances=1,
        misfire_grace_time=120,
    )

    if self_ping_func:
        async def keep_alive():
            try:
                await self_ping_func()
            except Exception:
                pass

        scheduler.add_job(
            keep_alive,
            trigger=IntervalTrigger(minutes=10, timezone=PKT),
            id="keep_alive",
            name="Self-ping Keep-Alive",
            replace_existing=True,
        )

    scheduler.start()
    logger.info("[Scheduler] Started. Next refresh in 1 hour.")
