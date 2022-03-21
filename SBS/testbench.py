from db import DB

db = DB()

salutation = input("Titel: ")
forename = input("Vorname: ")
surename = input("Nachname: ")
telephone = input("Telefon :")
email = input("EMail: ")

db.db_adduser(salutation, forename, surename, telephone, email)

vals = db.db_getAll()
print(vals)

