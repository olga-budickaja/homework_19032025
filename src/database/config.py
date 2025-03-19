import psycopg2

from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from database.queries import CREATE_COMMENTS_TABLE, CREATE_EMAILS_TABLE, CREATE_LIKES_TABLE, CREATE_POSTS_TABLE, CREATE_USERS_TABLE


connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

query_result_users = execute_query(
    connection=connection,
    query=CREATE_USERS_TABLE
)

query_result_posts = execute_query(
    connection=connection,
    query=CREATE_POSTS_TABLE
)

query_result_comments = execute_query(
    connection=connection,
    query=CREATE_COMMENTS_TABLE
)

query_result_emails = execute_query(
    connection=connection,
    query=CREATE_EMAILS_TABLE
)

query_result_likes = execute_query(
    connection=connection,
    query=CREATE_LIKES_TABLE
)
