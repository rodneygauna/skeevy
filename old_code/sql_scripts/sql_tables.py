"""
Python script to create and pre-load the data for testing.
"""
import sqlite3

# Drop all tables.
drop_tables_person = """
DROP TABLE IF EXISTS person;
"""

drop_tables_pet = """
DROP TABLE IF EXISTS pet;
"""

# Create the 'person' table.
create_table_person = """
CREATE TABLE IF NOT EXISTS person (
    id INTEGER NOT NULL PRIMARY KEY,
    firstname TEXT NOT NULL,
    middlename TEXT NULL,
    lastname TEXT NOT NULL,
    suffix TEXT NULL,
    email TEXT NOT NULL UNIQUE,
    status TINYINT(1) NOT NULL
);"""

# Add a person to the 'person' table.
insert_entry_person = """
INSERT INTO person (firstname, lastname, email, status) VALUES (
    'Rodney',
    'Gauna',
    'rodneygauna@gmail.com',
    1
);"""

# Create the 'pet' table.
create_table_pet = """
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    dateofbirth DATE NOT NULL,
    pettype TEXT NOT NULL,
    status TINYINT(1) NOT NULL
);"""

# Add a pet to the 'pet' table.
insert_entry_pet = """
INSERT INTO pet (name, dateofbirth, pettype, status) VALUES (
    'Boogie',
    '2013-04-20',
    'Dog',
    1
);"""

# Connect to the 'skeevy.db', create the tables and load the data.
with sqlite3.connect("skeevy.db") as connection:
    cursor = connection.cursor()
    cursor.execute(drop_tables_person)
    cursor.execute(drop_tables_pet)
    cursor.execute(create_table_person)
    cursor.execute(insert_entry_person)
    cursor.execute(create_table_pet)
    cursor.execute(insert_entry_pet)
