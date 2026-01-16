import sqlite3
from datetime import date

def get_conn():
    return sqlite3.connect("prices.db")

def save_price(product, prices):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS price_history
    (product TEXT, platform TEXT, price INTEGER, date TEXT)""")
    today = str(date.today())
    for platform, price in prices.items():
        if price:
            cur.execute("INSERT INTO price_history VALUES (?,?,?,?)",
                        (product, platform, price, today))
    conn.commit()
    conn.close()

def fetch_history(product):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT date, platform, price FROM price_history WHERE product=?",
                (product,))
    data = cur.fetchall()
    conn.close()
    return data
