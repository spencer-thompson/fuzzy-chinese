"""
Honors Contract for CS 3270
---

This file handles initializing the sqlite database.
"""

import sqlite3
from pathlib import Path


def init_db():
    """
    This function creates the `dict.db` sqlite database file and loads the
    database with the simplified/traditional characters, pinyin and definition
    """
    conn = sqlite3.connect("dict.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dict (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            simplified TEXT,
            traditional TEXT,
            pinyin TEXT,
            definition TEXT
        )
    """)

    with open("cedict_ts.u8", "r") as file:
        # reading line by line because when I didn't I almost crashed my browser lol
        for line in file:
            if line.startswith("#"):  # ignore comments / license
                continue
            l = line.split()
            trad = l[0]
            simp = l[1]
            total = ""
            end = 0
            for i, p in enumerate(l[2:], 2):
                if p.startswith("[") and p.endswith("]"):
                    total += p.strip("[]")
                    end = i
                    break
                elif p.startswith("["):
                    total += p.strip("[") + " "

                elif p.endswith("]"):
                    total += p.strip("]")
                    end = i
                    break
                else:
                    total += p + " "

            pinyin = total
            next = end + 1
            definition = " ".join(l[next:]).strip("\\/")

            cursor.execute(
                """
                INSERT INTO dict (simplified, traditional, pinyin, definition) VALUES
                    (?, ?, ?, ?)
                """,
                (
                    simp,
                    trad,
                    pinyin,
                    definition,
                ),
            )

    conn.commit()
    conn.close()


def query(where: str = ""):
    """
    This is just a simple function to query the database
    simpler than an ORM?
    """
    conn = sqlite3.connect("dict.db")
    cursor = conn.cursor()

    query = f"SELECT traditional, simplified, pinyin, definition FROM dict WHERE {where}"

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.commit()
    conn.close()

    return rows


def main():
    db_file = Path("./dict.db")

    if not db_file.exists():
        init_db()


if __name__ == "__main__":
    main()
