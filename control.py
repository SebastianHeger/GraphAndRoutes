from pathlib import Path
import sqlite3

from Graph import graphCreation

if __name__ == '__main__':
    db_path = Path() / 'database.db'
    with sqlite3.connect(db_path) as conn:
        graphCreation.database_reset(conn)
