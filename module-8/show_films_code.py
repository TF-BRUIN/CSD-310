import mysql.connector 
from mysql.connector import errorcode 
line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

pythonmysql = mysql.connector.connect(
	user="root", 
	password="RoyalRepublicHereICome4u+", 
	host="localhost", 
	database="movies"
)
cursor = pythonmysql.cursor()
#print(line_break)

def show_films(cursor, title):
	cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
	films = cursor.fetchall()
	print("\n -- {} --".format(title))
	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))















