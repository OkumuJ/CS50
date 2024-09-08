# sql code run via command line 

# starting sqlite 
sqlite3 read.db

# creating a new table 
CREATE TABLE books(
    # indent with space bar 4 spaces
    id INTEGER,
    title TEXT,
    publeished NUMERIC,
    rating INTEGER, 
    PRIMARY KEY(id)
);

# checking the table in the database 
 .tables

# checking the content of the table 
 .schema tables

ctrl L to clear the sqlite3 terminal 

# inserting to tables 
INSERT INTO books (title, published, rating)
VALUES ('flights', '2017-05-17', 4);

# incase of a mistake 
VALUES (;

# checking for the inserted values 
SELECT * FROM books;

# data deletion 
DELETE FROM books WHERE title = 'flghts';