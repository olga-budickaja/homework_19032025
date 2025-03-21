from database.config import connection, execute_query, execute_read_query
from database.queries import ADD_USER, GET_USER_BY_ID, GET_USERS, GET_USERS_BETWEEN_16_20
from database.data import users_data


def add_user():
    for user in users_data:
        execute_query(connection, ADD_USER, (user["firstname"], user["lastname"], user["email"], user["age"]))

def get_users():
    return execute_read_query(connection, GET_USERS)

def user_by_id(id:str):
    result = execute_read_query(connection, GET_USER_BY_ID, (id,))
    return result[0] if result else None

def users_between_16_20():
    return execute_read_query(connection, GET_USERS_BETWEEN_16_20)

users = get_users()
user = user_by_id(3)
users_16_20 = users_between_16_20()

print(users)
print(user)
print(users_16_20)
