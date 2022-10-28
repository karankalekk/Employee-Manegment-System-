#Sql Information
import mysql.connector

user = "root"
mypass = "karan"
DatabaseName = "Employee"



def startup():
        #Connecting mysql Server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="karan"
    )
    cursor = mydb.cursor()
    try:
        cursor.execute("CREATE DATABASE Employee")
        # print("success")
        cursor.execute("use Employee")
        # print("success2")
        cursor.execute("CREATE TABLE EmployeeData(Employeeid INT AUTO_INCREMENT PRIMARY KEY,Name varchar(50), post varchar(20), Gender varchar(10), Email varchar(60), Phone bigint, Address varchar(255))")
        # print("tbble creteesfhvehj")
    except:
        pass
