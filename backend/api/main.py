from fastapi import FastAPI
from backend.api.services import run_analysis_service
from backend.storage.result_store import load_results

app = FastAPI(title="Smart Data Monitor API")


@app.get("/")
def home():
    return {"message": "Smart Data Monitor API Running"}


@app.post("/analyze")
def trigger_analysis():
    result = run_analysis_service()
    return result


@app.get("/results")
def get_latest_result():
    results = load_results()
    if not results:
        return {"message": "No analysis done yet"}
    return results
