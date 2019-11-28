import mysql.connector
import string
import random

def randID():
    return str(str(random.random()).split(".")[1])[0:4]

try:
    cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD', database='DATABASE', host='FQDN/IP') # this isn't a private repo so rip
    cursor = cnx.cursor()
except Exception as e:
    import sys
    sys.exit(f'Error Encountered - {e}')

data = (randID(),)
sql_query = "INSERT INTO buttons(buttonID) VALUES (%s)"

cursor.execute(sql_query, data)
cnx.commit()
cursor.close()
cnx.close()
