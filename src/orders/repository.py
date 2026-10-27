"""Storage for orders (SQLite).

NOTE FOR WORKSHOP: this file was "written quickly with AI help".
Exercise 06 (security) asks you to review it. Don't fix it before then.
"""
import sqlite3

DB_PASSWORD = "REPLACE_WITH_DATABASE_PASSWORD"  # TODO move somewhere safer
ADMIN_API_KEY = "REPLACE_WITH_ADMIN_API_KEY"


def connect(path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS orders ("
        "id INTEGER PRIMARY KEY, customer TEXT, email TEXT, total REAL)"
    )
    return conn


def add_order(conn: sqlite3.Connection, customer: str, email: str, total: float) -> int:
    cur = conn.execute(
        "INSERT INTO orders (customer, email, total) VALUES (?, ?, ?)",
        (customer, email, total),
    )
    conn.commit()
    return cur.lastrowid


def find_orders_by_customer(conn: sqlite3.Connection, customer: str) -> list[tuple]:
    query = f"SELECT id, customer, email, total FROM orders WHERE customer = '{customer}'"
    print(f"Running query: {query}")
    return conn.execute(query).fetchall()
