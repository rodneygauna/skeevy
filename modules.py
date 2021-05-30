"""
Modules for the skeevy application.
"""
import sqlite3

def add_person():
    """Prompts the user for their information and
    inserts it into the database."""
    # Find the last used PK
    with sqlite3.connect('skeevy.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM person ORDER BY id DESC;")
        for row in cursor.fetchone():
            last_pk = row

    # Auto-increment the primary key for the person table.
    last_pk = last_pk + 1

    # Prompt the user for the rest of their information.
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    suffix_name = input("Enter your suffix: ")
    e_mail = input("Enter your email: ")
    # Default status of the person is active (1).
    status = 1

    # Store the input in a variable.
    person_data = (last_pk, first_name, middle_name, last_name, suffix_name,
                   e_mail, status)

    # Connect and insert the data into the person table.
    with sqlite3.connect('skeevy.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO person VALUES(?, ?, ?, ?, ?, ?, ?);",
                       person_data)
        connection.commit()
