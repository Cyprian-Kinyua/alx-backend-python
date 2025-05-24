import mysql.connector
# This script connects to a MySQL database and streams user data from the 'user_data' table.
def stream_users():
    conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ctripplek@14727', 
    database='ALX_prodev'
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data")

    for row in cursor.fetchall():
        yield row
   
    cursor.close()
    conn.close()

# Example usage:
for user in stream_users():
    print(user)