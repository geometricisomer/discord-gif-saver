"""
db.py

Handles connection with data base.
"""

import sqlite3
from main import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def setup():
    """
    Creates tables, if they do not exist already.

    Returns: 
        None
    """
    cur.execute("""
    CREATE TABLE IF NOT EXISTS gifs (
        uuid TEXT PRIMARY KEY,
        link TEXT,
        name TEXT,
        tags TEXT,
        added_by INTEGER,
        added_time INTEGER,
    )
    """)
    cur.execute()
