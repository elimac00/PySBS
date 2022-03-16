import sqlite3
from db import DB

db = DB()
#Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

#SQL-Abfrage
sql = "SELECT * FROM mitarbeiter"

#Kontrollausgabe der SQL-ABfrage
#print(sql)

#Absenden der SQL-Abfrage
#Empfang des Ergebnisses
#self.__cursor.execute(sql)

#Ausgabe des Ergebnisses
for dsatz in cursor:
    print(dsatz[0], dsatz[1], dsatz[2],
          dsatz[3], dsatz[4], dsatz[5], dsatz[6], dsatz[7])

#Verbindung beenden
connection.close()