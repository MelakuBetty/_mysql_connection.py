import mysql.connector


class DB():
    mydb = my_conenct = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="betty1234",
          database="sakila"
        )

    def connect(self, sql, q_type):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        if q_type == 'select':
            return mycursor.fetchall()
        else:
            return self.mydb.commit()
