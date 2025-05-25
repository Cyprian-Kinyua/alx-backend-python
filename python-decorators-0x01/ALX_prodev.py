import sqlite3
import os

if os.path.exists('users.db'):
    os.remove('users.db')
try: 
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    print("Database created successfully")

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    conn.commit()
    print("Table created successfully")

    # Insert data into the table
    users = [
        ("Alice", "alice@example.com", 30.0),
        ("Bob", "bob@example.com", 25.0),
        ("Charlie", "charlie@example.com", 28.0),
        ("David", "david@example.com", 35.0),
        ("Eve", "eve@example.com", 22.0),
        ("Frank", "frank@example.com", 40.0),
    ]

    cursor.executemany('''
    INSERT INTO users (name, email, age) VALUES (?, ?, ?)
    ''', users)
    conn.commit()
    print("Data inserted successfully")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    if cursor:
        cursor.close()
        print("Cursor closed")
    if conn:
        conn.close()
        print("Connection closed")
    
