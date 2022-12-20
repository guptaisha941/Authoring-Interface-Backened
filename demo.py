import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ishagu@1",
    database="testdb")

mycursor=mydb.cursor()


# mycursor.execute("CREATE TABLE demo (name VARCHAR(255), age INTEGER(10))")

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1)

mydb.commit()

# mycursor.execute("SHOW TABLES")

# for db in mycursor:
#     print(db)