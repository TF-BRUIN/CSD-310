import mysql.connector 
from mysql.connector import errorcode 

line_break = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

pythonmysql = mysql.connector.connect(
	user="root", 
	password="RoyalRepublicHereICome4u+", 
	host="localhost", 
	database="movies"
)

mycursor = pythonmysql.cursor()

print(line_break)
mycursor.execute("SELECT * FROM film")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

print(line_break)
mycursor.execute("SELECT * FROM genre")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

print(line_break)
mycursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

print(line_break)
mycursor.execute("SELECT film_director, film_name FROM film")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

print(line_break)
pythonmysql.close()






