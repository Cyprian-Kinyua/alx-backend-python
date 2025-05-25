import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        print("[INFO] Connecting to database...")
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        
        print(f"[INFO] Executing query: {self.query} | Params: {self.params}")
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        
        return self.results  # Yield the results to the with-block

    def __exit__(self, exc_type, exc_value, traceback):
        print("[INFO] Closing database connection...")
        if self.conn:
            self.conn.close()
        if exc_type:
            print("[ERROR]", exc_value)

query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery("users.db", query, params) as users:
    print("\n📄 Users over age 25:")
    for user in users:
        print(user)
