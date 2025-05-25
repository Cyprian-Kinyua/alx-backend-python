import sqlite3

class Databaseconn:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        print("[INFO] Opening database conn")
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        print("[INFO] Closing database conn")
        if self.conn:
            self.conn.close()
        if exc_type is not None:
            print(f"[ERROR] An error occurred: {exc_value}")

with Databaseconn("users.db") as cursor:
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\n users:")
    for user in users:
        print(user)