from tkinter import *
from tkinter.ttk import *
import mysql.connector
from config import *
import csv


def exportData(root,Canvas3):
    mydb = mysql.connector.connect(
        user=user,
        host="localhost",
        password=mypass
    )
    cursor = mydb.cursor()
    try:
        cursor.execute("use Employee;")
        cursor.execute("select * from employeeData")
        result = cursor.fetchall()
        exportdata = csv.writer(open("Employeedata.csv","w"))
        exportdata.writerow(("Employeeid","Name","Post","Gender","Email","Phone","Address"))
        for row in result:
            exportdata.writerow(row)
        progress = Label(Canvas3,text="Data Exported to CSV File")
        progress.place(x=200,y=600)
        progress.after(3000,progress.place_forget)
    except:
        progress = Label(Canvas3,text="Error Exporting Data to CSV File")
        progress.place(x=200,y=600)
        progress.after(3000,progress.place_forget)
    

