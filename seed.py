# This script creates a MySQL database named 'ALX_prodev' if it does not already exist.
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ctripplek@14727',
)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS ALX_prodev")  # Drop the database if it exists
cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")

print("Database created successfully")

cursor.close()
conn.close()



#Creating a table and seeding it with data
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ctripplek@14727',
    database='ALX_prodev'
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data (
    user_id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age DECIMAL NOT NULL
)
""")
print("Table created successfully")

# Inserting sample data into the table
users = [
    ("Alice", "alice@example.com", 30.0),
    ("Bob", "bob@example.com", 25.0),
    ("Charlie", "charlie@example.com", 28.0),
    ("David", "david@example.com", 35.0),
    ("Eve", "eve@example.com", 22.0),
]

cursor.executemany("""
INSERT INTO user_data (name, email, age)
VALUES (%s, %s, %s)
""", users)

conn.commit()
print("Sample data inserted successfully")
cursor.close()
conn.close()