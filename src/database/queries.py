CREATE_USERS_TABLE = '''
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(20) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age NUMERIC(3,0) CHECK (age BETWEEN 16 AND 90)
);
'''

CREATE_IMAGE_TABLE = '''
CREATE TABLE IF NOT EXISTS images (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    url VARCHAR(100) NOT NULL,
    price NUMERIC(3,2) CHECK (price BETWEEN 0 AND 100000)
);
'''

GET_USERS = '''
SELECT * FROM users;
'''

GET_USERS_BETWEEN_16_20 = '''
SELECT firstname, lastname
FROM users
WHERE age BETWEEN 16 AND 20;
'''

GET_USER_BY_ID = '''
SELECT * FROM users
WHERE id = %s
'''

ADD_USER = '''
INSERT INTO users (firstname, lastname, email, age)
VALUES (%s, %s, %s, %s);
'''
