from dbPySBS import DB

dbPySBS = DB()
pk = dbPySBS.add_Customer("Mrs", "Eva", "Mueller", "091765432", "eva.mueller@sbs.de", "91096 Haurach", "Schaeffler")
dbPySBS.delete_Customer(pk)
results = dbPySBS.search("Max")
print(results)

