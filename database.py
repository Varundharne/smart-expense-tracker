import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

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
