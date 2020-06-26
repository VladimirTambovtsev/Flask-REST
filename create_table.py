import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)


# # create
# user = (1, 'me', '123')
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)

# # create many
# users = [
#     (2, 'me2', '123'),
#     (3, 'me3', '123'),
#     (4, 'me4', '123'),
# ]
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.executemany(insert_query, users)

# # select all
# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

connection.commit()
connection.close()
