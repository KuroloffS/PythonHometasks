import sqlite3


def create_table():
    connection = sqlite3.connect("roster.db")

    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = "Create table Roster(name TEXT, Species TEXT, Age INTEGER);"
        data = cursor.execute(query)


def insert_data():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = (
            "Insert into Roster Values('Benjamin Sisko', 'Human', 40),"
            "('Jadzia Dax',' Trill', 300),"
            "('Kira Nerys', 'Bajoran', 29);"
        )
        cursor.execute(query)


def update_data():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = "Update Roster set name='Ezri Dax' where name='Jadzia Dax';"
        cursor.execute(query)


def get_name_age():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = "SELECT name, age FROM Roster WHERE species='Bajoran';"
        data = cursor.execute(query)
        print(data.fetchall())


def remove_above_100():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = "DELETE FROM Roster WHERE age>=100;"
        cursor.execute(query)


def add_table_rank():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE Roster ADD COLUMN rank TEXT;")
        queries = [
            "UPDATE Roster SET rank='Major' WHERE name='Kira Nerys';",
            "UPDATE Roster SET rank='Lieutenant' WHERE name='Ezri Dax';",
            "UPDATE Roster SET rank='Captain' WHERE name='Benjamin Sisko';",
        ]
        for query in queries:
            cursor.execute(query)


def get_ordered_age():
    with sqlite3.connect("roster.db") as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM Roster ORDER BY age DESC;"
        data = cursor.execute(query)
        print(data.fetchall())


if __name__ == "__main__":
    create_table()
    insert_data()
    update_data()
    get_name_age()
    remove_above_100()
    add_table_rank()
    get_ordered_age()
