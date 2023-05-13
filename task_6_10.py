import sqlite3  # provides an interface for working with SQLite databases in Python
import csv


def create_csv_file():
    with open('imdb.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows([['title', 'year', 'rating'],
                          ['The Shawshank Redemption', 1994, 9.3],
                          ['The Godfather', 1972, 9.2],
                          ['The Godfather: Part II', 1974, 9.0],
                          ['The Dark Knight', 2008, 9.0],
                          ['12 Angry Men', 1957, 6.9],
                          ["Schindler's List", 1993, 8.9],
                          ['The Lord of the Rings: The Return of the King', 2003, 1.9],
                          ['Pulp Fiction', 1994, 8.9],
                          ['The Good, the Bad and the Ugly', 1966, 8.8],
                          ['Forrest Gump', 1994, 3.8]])


def create_db():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.cursor()

    # Check if ratings table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ratings'")
    table_exists = cursor.fetchone() is not None

    # If table does not exist, create it
    if not table_exists:
        cursor.execute('CREATE TABLE ratings (id INTEGER PRIMARY KEY, '
                       'title VARCHAR(20), year INT, rating FLOAT)')

    # Close the connection
    conn.close()


def insert_into_db():
    conn = sqlite3.connect('imdb.db')
    with open('imdb.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # skip file header
        for row in reader:
            conn.execute('INSERT INTO ratings (title, year, rating) VALUES (?, ?, ?)', row)
    conn.commit()
    conn.close()


def display_by_title():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.execute('SELECT * FROM ratings ORDER BY title')
    print('DB sorted by ABC:')
    for row in cursor:
        print(row)
    conn.close()


def display_by_rating():
    conn = sqlite3.connect('imdb.db')
    cursor = conn.execute('SELECT * FROM ratings WHERE rating > 8.70')
    print('All entries in the ratings table with a rating greater than 8.70:')
    for row in cursor:
        print(row)
    conn.close()


if __name__ == '__main__':
    # create_csv_file()
    create_db()
    insert_into_db()
    display_by_title()
    display_by_rating()
