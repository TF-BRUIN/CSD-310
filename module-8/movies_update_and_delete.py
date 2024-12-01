import mysql.connector 
from mysql.connector import errorcode 
from show_films_code import show_films
line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
pythonmysql = mysql.connector.connect(
	user="root", 
	password="RoyalRepublicHereICome4u+", 
	host="localhost", 
	database="movies"
)
cursor = pythonmysql.cursor()
print(line_break)

show_films(cursor,"DISPLAYING FILMS")

cursor.execute("INSERT INTO genre(genre_name) VALUES ('Comedy')")
cursor.execute("INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES('Home Alone', '1990', '103', 'Chris Columbus', (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'), (SELECT genre_id FROM genre WHERE genre_name = 'Comedy'))")
show_films(cursor,"DISPLAYING FILMS AFTER INSERT")

cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
show_films(cursor,"DISPLAYING FILMS AFTER UPDATING ALIEN TO HORROR")

cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'") 
show_films(cursor,"DISPLAYING FILMS AFTER DROPPING GLADIATOR")











