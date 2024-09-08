loading data into the SQLITE db 
>sqlite3 favorites.db
>> .mode csv
>> .import favorites.csv favorites
>> .quit
>> .schema //checks the 
>> ctrl L //to clear the terminal
SELECT COUNT (*) FROM favorites;
select distinct (language) from favorites;
select count(distinct (language)) from favorites;

SELECT COUNT (*) FROM favorites WHERE language = 'C';
SELECT COUNT (*) FROM favorites WHERE language = 'C' AND problem = 'Hello, world';
SELECT language, COUNT (*) FROM favorites GROUP BY language ORDER BY COUNT(*)
SELECT language, COUNT (*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC


CREATING TABLE 
INSERT INTO favorites (language, problem ) VALUES ('SQL', 'Fifty ville');

DELETE
DELETE FROM WHERE CONDITION 
DELETE FROM favorites WHERE Timestamp IS NULL;


UPADTING TEH TABLE 
>UPDATE table SET column = value WHERE condition;
UPDATE favorites SET language = 'SQL', problem = 'fiftyville';


IMdb //IMDb.com
nested quesry 
joining table 
indexes