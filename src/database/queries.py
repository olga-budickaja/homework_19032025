CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender VARCHAR(255),
        nationality VARCHAR(255)
    );
'''

CREATE_POSTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        user_id INT,
        title VARCHAR(255),
        description VARCHAR(255)
    );
'''

CREATE_COMMENTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS comments (
        id SERIAL PRIMARY KEY,
        user_id INT,
        post_id INT,
        text TEXT
    );
'''

CREATE_LIKES_TABLE = '''
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INT,
        post_id INT
    );
'''

CREATE_EMAILS_TABLE = '''
    CREATE TABLE IF NOT EXISTS emails (
        id SERIAL PRIMARY KEY,
        user_id INT,
        email TEXT
    );
'''
