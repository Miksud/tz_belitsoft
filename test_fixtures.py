import shutil
import pytest
import sqlite3
import os
# с болью и слезами юзая гугл пишем эти тесты
@pytest.fixture(scope="module")
def test_bd():
    test_bd = 'backup_copy.db'

    shutil.copyfile('backup.db', test_bd)

    connection = sqlite3.connect(test_bd)

    yield connection

    connection.close()
    os.remove(test_bd)

def test_insert_book(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES ('qwe_title', 'qwe_author', 123)")
    test_bd.commit()
    cursor.execute("SELECT COUNT(*) FROM books WHERE title='qwe_title'")
    count = cursor.fetchone()[0]
    assert count == 1

def test_select_all(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    test_bd.commit()

def test_delete_book(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("DELETE FROM books WHERE title='qwe_title';")
    test_bd.commit()
    cursor.execute("SELECT COUNT(*) FROM books WHERE title='qwe_title'")
    count = cursor.fetchone()[0]
    assert count == 0

def test_updated_title(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("UPDATE books SET title = 'updated_name' WHERE title = 'book1' OR author = 'author2';")
    test_bd.commit()
    cursor.execute("SELECT COUNT(*) FROM books WHERE title='updated_name'")
    count = cursor.fetchone()[0]
    assert count == 2

def test_check_not_book(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("SELECT COUNT(*) FROM books WHERE title='dfghjkl'")
    count = cursor.fetchone()[0]
    assert count == 0

def test_check_no_valid_data(test_bd):
    cursor = test_bd.cursor()
    cursor.execute("SELECT COUNT(*) FROM books where year = 0")
    count = cursor.fetchone()[0]
    assert count == 0




