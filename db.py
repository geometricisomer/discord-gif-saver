"""
db.py

Handles connection with data base.
"""

import sqlite3
from main import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False) # type: ignore
conn.execute("PRAGMA foreign_keys = ON")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

def setup():
    """
    Creates table, if it does not exist already.
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
    conn.commit()

def gif_add():
    """
    Adds a gif to data base.

    Parameters:
        link (str): URL link of the gif.
        name (str): Name for the gif.
        tags (str): tags assosiated with the gif (lowercase letters and underscores only, separeted by spaces).
        author (int): Discord User ID of person that added the gif.
    
    """
    pass

def gif_edit():
    pass

def gif_delete():
    pass

def gif_find():
    pass

def gif_dump():
    pass

