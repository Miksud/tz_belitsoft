import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER not NULL
)
''')

cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', ('book1', 'author1', 1))
cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', ('book2', 'author2', 5))
cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', ('book3', 'author3', 15))
cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', ('book4', 'author4', 1))
cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', ('book5', 'author5', 10))

connection.commit()
connection.close()


connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('SELECT * from Books;', )
results = cursor.fetchall()

for row in results:
  print(row)

connection.close()



