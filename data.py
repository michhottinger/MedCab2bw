#imports
import sqlite3


#connect to db
conn = sqlite3.connect('data.db')

#create a function to query data
def q_all(query):
    curs = conn.cursor()
    curs.execute(query)
    rows = curs.fetchall()
    curs.close()
    return rows

def q_one(query):
    row = q_all(query)
    return row[0][0]
#Create the table via function
