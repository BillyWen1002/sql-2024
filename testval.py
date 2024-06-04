import sqlite3

DATABASE = "valorant.db"

db = sqlite3.connect('valorant.db')
cursor = db.cursor()
sql = "SELECT * from agents;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
