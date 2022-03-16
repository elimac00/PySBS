import sqlite3, os, sys
from cr_sqlite3

#Existenz feststellen
if os.path.exists("firma.db"):
    print("Datei bereits vorhanden")
    sys.exit(0)

#Verbindung zur Datenbank erzeugen
connection = sqlite3.connect("firma.db")

#Datensatz Coursor erzeugen
cursor = connection.cursor()

#Datenabnktabelle erzeugen
sql = "CREATE TABLE mitarbeiter (" \
    "pk INTEGER PRIMARY KEY NOT NULL,  " \
    "salutation TEXT, " \
    "forename TEXT NOT NULL, " \
    "surname TEXT NOT NULL, " \
    "telephone INT, " \
    "email TEXT, " \
    "foreign_key_co INTEGER NOT NULL, "
cursor.execute(sql)


#äDatensatz erzeugen
sql = "INSERT INTO mitarbeiter VAlUES (1," \
    'Herr', 'Matthias', 'Schröder', 09178947385, 'schröder.matthias@gmx.de', 1)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO mitarbeiter VAlUES (2," \
    'Frau', 'Karina', 'Klemma', 083849375, 'karina.klemma@gmx.de', 2)"
cursor.execute(sql)
connection.commit()

sql = "INSERT INTO mitarbeiter VAlUES (3," \
    'Herr', 'Max', 'Gold', 0991738493, 'max.gold@gmx.de', 3)"
cursor.execute(sql)
connection.commit()

#Verbindung beenden
connection.close()

