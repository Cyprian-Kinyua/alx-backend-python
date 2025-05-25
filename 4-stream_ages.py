import mysql.connector

def stream_user_ages():
    connection = None
    cursor = None
    connection = mysql.connector.connect(       
        host='localhost',
        user='root',
        password='Ctripplek@14727',
        database='ALX_prodev',
    )

    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age

    cursor.close()
    connection.close()  

# Example usage:
print("User ages:")
for age in stream_user_ages():
    print(age)

def average_age_of_users():
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    average_age = total_age / count if count > 0 else 0
    return average_age

# Example usage of average_age
print("Average age of users: ", average_age_of_users()) 

