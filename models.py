# models.py
import sqlite3

def initDb():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date date NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        description TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def addTransaction(date, category, amount, description):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transactions (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    
    conn.commit()
    conn.close()

def queryTransactions(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
