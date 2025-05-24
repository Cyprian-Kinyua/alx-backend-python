import mysql.connector

def paginate_users(page_size, offset=0):
    conn = None
    cursor = None
    conn = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = 'Ctripplek@14727',
        database = 'ALX_prodev'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))

    users = cursor.fetchall()
    cursor.close() 
    conn.close()
    return users

# Example usage:
print("Paginated users", paginate_users(page_size=3, offset=0))

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

# Example usage of lazy_paginate
for page in lazy_paginate(page_size=3):
    print("Page of users:", page)
    