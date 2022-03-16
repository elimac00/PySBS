import sqlite3, os, sys

connection = None
cursor = None

class DB:
    def __init__(self):
        global connection
        connection = sqlite3('firma.db')
        self.__cursor = connection.cursor()

        self.__cursor.execute('''
        
            "CREATE TABLE mitarbeiter (" \
                "pk INTEGER PRIMARY KEY NOT NULL,  " \
                "salutation TEXT, " \
                "forename TEXT NOT NULL, " \
                "surname TEXT NOT NULL, " \
                "telephone INT, " \
                "email TEXT, " \
                "foreign_key_co INTEGER NOT NULL, ''')



    def db_adduser(self):
        global cursor
        global connection

        cursor.execute('''
        "INSERT INTO mitarbeiter VAlUES (1," \
        'Herr', 'Matthias', 'Schröder', 09178947385, 'schröder.matthias@gmx.de', 1)
        ''')
        connection.commit()


    def db_getAll(self):
        global cursor
        cursor.execute('''
        SELECT * FROM mitarbiter
        ''')
        ret = (cursor.fetchall())
        return ret
