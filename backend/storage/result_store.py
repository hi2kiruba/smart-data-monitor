import aiosqlite
from backend.storage.db_setup import DB_PATH


async def save_results(meter_id, date, count):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO readings (meter_id, reading_date, reading_count) VALUES (?, ?, ?)",
            (meter_id, date, count)
        )
        await db.commit()


async def get_results():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT meter_id, reading_date, reading_count FROM readings ORDER BY id DESC")
        rows = await cursor.fetchall()
        return [
            {"meter_id": r[0], "date": r[1], "reading_count": r[2]}
            for r in rows
        ]


async def get_dashboard_metrics():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT meter_id, SUM(reading_count) FROM readings GROUP BY meter_id")
        rows = await cursor.fetchall()

        labels = [r[0] for r in rows]
        counts = [r[1] for r in rows]

        return {
            "labels": labels,
            "counts": counts
        }
