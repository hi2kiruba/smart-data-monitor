from datetime import datetime
from backend.storage.result_store import save_results


async def run_analysis_service():
    meter_id = "METER001"
    date = datetime.now().strftime("%Y-%m-%d")
    count = 7

    await save_results(meter_id, date, count)

    return {"meter_id": meter_id, "date": date, "count": count}
