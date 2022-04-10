import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="************",
  database="sakila"
)

mycursor = mydb.cursor()
sql = "SELECT first_name, last_name FROM actor ORDER BY first_name ASC LIMIT 5"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
