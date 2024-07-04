import sqlite3
# чекаем что в бэкапе лежит
connection = sqlite3.connect('backup.db')
cursor = connection.cursor()

cursor.execute('SELECT * from Books;', )
results = cursor.fetchall()

for row in results:
  print(row)

connection.close()