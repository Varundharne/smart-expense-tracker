import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Expenses table
cur.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    category TEXT,
    description TEXT
)
""")

# Budget table
cur.execute("""
CREATE TABLE IF NOT EXISTS budget(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL
)
""")

conn.commit()
conn.close()

print("Tables created successfully.")
