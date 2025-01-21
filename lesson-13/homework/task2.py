import sqlite3


def create_table():
  connection = sqlite3.connect("library.db")
  with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor()
    query = "CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT);"
    data = cursor.execute(query)
def insert_data():
  with sqlite3.connect("library.db") as conn:
    cursor = conn.cursor
    query = (
      "INSERT INTO Books VALUES('Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),"
      "('1984', 'George Orwell', 1949, 'Dystopian'),"
      "('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic'),"
    )
    cursor.execute(query)
if __name__ == "__main__":
    create_table()
    insert_data()