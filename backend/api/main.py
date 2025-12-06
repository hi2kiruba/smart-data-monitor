from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

from backend.storage.db_setup import init_db
from backend.api.services import run_analysis_service
from backend.storage.result_store import get_results, get_dashboard_metrics
from backend.scheduler.scheduler import start_scheduler


app = FastAPI(title="Smart Data Monitor API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATE_DIR)


@app.on_event("startup")
async def startup():
    await init_db()
    start_scheduler()


@app.get("/")
def home():
    return {"message": "Smart Data Monitor API Running"}


@app.post("/analyze")
async def trigger_analysis():
    return await run_analysis_service()


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    results = await get_results()
    metrics = await get_dashboard_metrics()

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": results, "metrics": metrics}
    )
