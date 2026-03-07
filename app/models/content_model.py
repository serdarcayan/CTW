"""
{
    "id": 0
    "title": "",
    "source_type": "web",
    "fetch_mode": "manual",
    "duration": 600,
    "url": "",
    "xpaths": [],
    "cache_policy": "save_all",
    "created_at": "2026-02-23T21:12:28.005800"
}
"""
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("app/data/cache.db")


class ContentModel:
    TABLE_NAME = "contents"

    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._ensure_table()

    # ======================================================
    # DATABASE INIT
    # ======================================================
    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _ensure_table(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                source_type TEXT NOT NULL,
                fetch_mode TEXT NOT NULL,
                duration INTEGER NOT NULL,
                url TEXT,
                xpaths TEXT,
                cache_policy TEXT,
                created_at TEXT NOT NULL
            )
        """
        )
        conn.commit()
        conn.close()

    # ======================================================
    # CREATE
    # ======================================================
    def create(self, item: dict):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute(
            f"""
            INSERT INTO {self.TABLE_NAME} 
            (title, source_type, fetch_mode, duration, url, xpaths, cache_policy, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                item.get("title", ""),
                item.get("source_type", "web"),
                item.get("fetch_mode", "manual"),
                item.get("duration", 600),
                item.get("url", ""),
                ",".join(item.get("xpaths", [])),
                item.get("cache_policy", "save_all"),
                item.get("created_at", datetime.now().isoformat()),
            ),
        )

        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    # ======================================================
    # READ
    # ======================================================
    def read(self, content_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE id=?", (content_id,))
        row = cursor.fetchone()
        conn.close()
        if not row:
            return None
        return self._row_to_dict(row)

    # ======================================================
    # READ ALL
    # ======================================================
    def read_all(self):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME} ORDER BY id ASC")
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_dict(row) for row in rows]

    # ======================================================
    # UPDATE
    # ======================================================
    def update(self, content_id: int, **kwargs):
        if not kwargs:
            return False

        columns = []
        values = []
        for key, value in kwargs.items():
            if key == "xpaths" and isinstance(value, list):
                value = ",".join(value)
            columns.append(f"{key}=?")
            values.append(value)

        values.append(content_id)

        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE {self.TABLE_NAME} SET {', '.join(columns)} WHERE id=?",
            values,
        )
        conn.commit()
        updated = cursor.rowcount
        conn.close()
        return updated > 0

    # ======================================================
    # DELETE
    # ======================================================
    def delete(self, content_id: int):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (content_id,))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()
        return deleted > 0

    # ======================================================
    # HELPER: ROW → DICT
    # ======================================================
    def _row_to_dict(self, row):
        return {
            "id": row[0],
            "title": row[1],
            "source_type": row[2],
            "fetch_mode": row[3],
            "duration": row[4],
            "url": row[5],
            "xpaths": row[6].split(",") if row[6] else [],
            "cache_policy": row[7],
            "created_at": row[8],
        }
