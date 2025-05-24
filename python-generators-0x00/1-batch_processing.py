import mysql.connector

def stream_users_in_batches(batch_size):
    conn = None
    cursor = None
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ctripplek@14727',
        database='ALX_prodev'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_data")
    

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    conn.close()

# Example usage:
print("Users in batches of 5:")
for batch in stream_users_in_batches(5):
    print(batch)

# filtering users by age
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user[3] > 25:  # Age is the third column
                return(user)

# Example usage of batch_processing
print("Users older than 25:")
for user in batch_processing(5):
    print(user)