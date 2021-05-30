import sqlite3

create_table_person = """
CREATE TABLE IF NOT EXISTS person(
    id INTEGER NOT NULL PRIMARY KEY,
    firstname TEXT NOT NULL,
    middlename TEXT NULL,
    lastname TEXT NOT NULL,
    suffix TEXT NULL,
    email TEXT NOT NULL UNIQUE,
    status TINYINT(1) NOT NULL
);"""

insert_entry_person = """
INSERT INTO person (firstname, lastname, email, status) VALUES (
    'Rodney',
    'Gauna',
    'rodneygauna@gmail.com',
    1
);"""

with sqlite3.connect("skeevy.db") as connection:
    cursor = connection.cursor()
    cursor.execute(create_table_person)
    cursor.execute(insert_entry_person)
