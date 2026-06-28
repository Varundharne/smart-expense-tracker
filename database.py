import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL
)
""")

conn.commit()
conn.close()

print("Budget table created successfully.")
