/* Drops all tables */
DROP TABLE IF EXISTS person;

/* Create the person table */
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    middlename TEXT NULL,
    lastname TEXT NOT NULL,
    suffix TEXT NULL,
    email TEXT NOT NULL UNIQUE,
    status TINYINT(1) NOT NULL 
);

/* Add test data into the person table */
INSERT INTO person (firstname, lastname, email, status)
VALUES
('Rodney', 'Gauna', 'rodneygauna@gmail.com', 1),
('Jaclyn', 'McGregor', 'jaclynmcgregor@gmail.com', 1),
('Max', 'Gauna', 'maxjamesgauna@gmail.com', 1),
('NoneActive', 'Person', 'notactive@fakemail', 0);

INSERT INTO person (firstname, middlename, lastname, email, status)
VALUES
('Sean', 'Steve', 'Simpson', 'III', 'seansteve@fakemail', 1),
('Mary', 'Jean', 'Gary', 'Jr', 'maryjane@fakemail', 0);