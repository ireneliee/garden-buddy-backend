import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password'
)

DATABASE_NAME = "GARDEN_BUDDY_BACKEND"
cursor = connection.cursor()

drop_database_query = "DROP DATABASE IF EXISTS " + DATABASE_NAME
cursor.execute(drop_database_query)

create_database_query = "CREATE DATABASE IF NOT EXISTS " + DATABASE_NAME
cursor.execute(create_database_query)

use_database_query = "USE " + DATABASE_NAME
cursor.execute(use_database_query)

# Create user table
create_user_query = '''
CREATE TABLE user (
    userId INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    userStartDate DATETIME
);
'''

cursor.execute(create_user_query)

# Inserting a new user
sql = 'INSERT INTO user (username, password, firstName, lastName, userStartDate) VALUES (%s, %s, %s, %s, now())'
val_1 = ('ireneliee', 'password', 'Irene', 'Lie')
cursor.execute(sql, val_1)
print(cursor.rowcount, 'record inserted.')
