from backend.api.services import run_analysis_service
from fastapi import FastAPI

app = FastAPI(title="Smart Data Monitor API")


@app.get("/")
def home():
    return {"message": "Smart Data Monitor API Running"}


@app.post("/analyze")
def trigger_analysis():
    result = run_analysis_service()
    return result
