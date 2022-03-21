import sqlite3

connection = None
cursor = None

class DB:
    def __init__(self):
        global connection
        self.connection = sqlite3.connect('firma.db')
        global cursor
        self.__cursor = self.connection.cursor()

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS mitarbeiter
            (pk INTEGER PRIMARY KEY NOT NULL,   
            salutation TEXT,  
            forename TEXT NOT NULL,
            surname TEXT NOT NULL,
            telephone INT,
            email TEXT, 
            foreign_key_co INTEGER NOT NULL)
             ''')

        self.connection.commit()



    def db_adduser(self, salutation, forename, surname, telephone, email):
        global cursor
        global connection

        #cursor.execute('''
        #"INSERT INTO mitarbeiter VAlUES (1," \
        #'Herr', 'Matthias', 'Schröder', 09178947385, 'schröder.matthias@gmx.de', 1)
        #''')

        cursor.execute('''
        INSERT INTO mitarbeiter (salutation,forename, surname, telephone, email) VALUES ("{}", "{}");
        '''.format(salutation,forename,surname,telephone,email))

        self.connection.commit()


    def db_getAll(self):
        global cursor
        cursor.execute('''
        SELECT * FROM mitarbiter
        ''')
        ret = cursor.fetchall()
        return ret
    
    def db_close(self):
        global cursor
        global connection
        
        self.cursor.close()
        self.connection.close()

    def search(self):
        global cursor
        global connection
        print("Es funktioniert!!!")

