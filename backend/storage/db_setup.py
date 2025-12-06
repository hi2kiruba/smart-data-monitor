import aiosqlite
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "results.db")


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meter_id TEXT NOT NULL,
                reading_date TEXT NOT NULL,
                reading_count INTEGER NOT NULL
            )
        """)
        await db.commit()
