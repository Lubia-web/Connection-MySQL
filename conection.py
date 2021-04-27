Import mysql.conector
connection = mysqul.conector.conector(host="localhost",user"root", passwd="")

cursor= connection.cursor()
cursor.execute("show databases")

for base in cursor:
    print(base)

connection.close()