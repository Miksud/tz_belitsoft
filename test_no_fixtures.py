import sqlite3
# лично я бы делал в таком формате тесты, которые сразу идут на тестовый стейдж, без использования фикстур, хотя с фикстурами тоже интересно получилось
def test_select_author4():
    connection = sqlite3.connect('backup.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books WHERE author='author4';")
    count_select_author = cursor.fetchone()[0]
    connection.close()

    assert count_select_author == 1


