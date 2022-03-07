import sqlite3

class DB:
    #Konstruktor
    def __init__(self):
        pass
        print("Konstruktor wurde aufgerufen!")
        self.__connection = sqlite3.connect()
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXIST scorelist
        (pk INTEGER PRIMARY KEY NOT NULL, pname TEXT, score INTEGER);
        ''')

        self.__connection.commit()

    def add_Customer(self, title, firstname, lastname, telephone, e_mail, address, company_name):
        return 0

    def delete_Customer(self, pk):
        pass

    def search(self, str):
        return(1,2,3,4,5,6,7,8)

    def get_costumer(self, pk):
        return

