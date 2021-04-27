import sqlite3

conn = sqlite3.connect('skeevy.db')
c = conn.cursor()

def create_table_person():
    c.execute('CREATE TABLE IF NOT EXISTS person(id INTEGER NOT NULL PRIMARY KEY, firstname TEXT NOT NULL, middlename TEXT NULL, lastname TEXT NOT NULL, suffix TEXT NULL, email TEXT NOT NULL UNIQUE, status TINYINT(1) NOT NULL);')
    
def data_entry_person():
    c.execute("INSERT INTO person (firstname, lastname, email, status) VALUES ('Rodney', 'Gauna', 'rodneygauna@gmail.com', 1);")
    conn.commit()
    c.close()
    conn.close()

create_table_person()
data_entry_person()