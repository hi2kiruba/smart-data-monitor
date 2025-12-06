from apscheduler.schedulers.asyncio import AsyncIOScheduler
from backend.api.services import run_analysis_service

scheduler = AsyncIOScheduler()


def start_scheduler():
    scheduler.add_job(run_analysis_service, "interval", minutes=1)
    scheduler.start()
