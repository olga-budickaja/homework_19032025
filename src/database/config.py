import psycopg2

from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from database.queries import CREATE_IMAGE_TABLE, CREATE_USERS_TABLE


connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def execute_read_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()

query_result_users: None = execute_query(
    connection=connection,
    query=CREATE_USERS_TABLE
)

query_result_images = execute_query(
    connection=connection,
    query=CREATE_IMAGE_TABLE
)

print(query_result_users)
