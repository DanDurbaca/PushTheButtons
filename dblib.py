import mysql.connector
import string

class buttonDBLib:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='button', password='buttonpress', database='button', host='5.189.155.63')
        self.cursor = cursor = self.cnx.cursor()

    def handleButton(self, button_id):
        sql_query = "INSERT INTO buttons(buttonID) VALUES (%s)"
        data = (button_id,) # dont remove comma
        self.cursor.execute(sql_query, data)
        self.cnx.commit()

    def handleScore(self, username, total_score):
        sql_query = "INSERT INTO scores(username, score) VALUES (%s, %s)"
        data = (username, total_score) # dont remove comma
        self.cursor.execute(sql_query, data)
        self.cnx.commit()

    def endConnection(self):
        self.cursor.close()
        self.cnx.close()
