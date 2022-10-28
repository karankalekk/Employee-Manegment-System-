from tkinter import *
from tkinter.ttk import *
import mysql.connector
from config import *

def searchData(root,Canvas2=None):
    from home import Homepage
    if(Canvas2!=None):
        Canvas2.destroy()
    
    root.title("Employee Data - Search Employee")
    root.geometry("900x700")
    icon = PhotoImage(file="assets\icon.png")
    root.iconphoto(False,icon)

    Canvas4 = Canvas(root)
    Canvas4.config(bg="#0d335d")
    Canvas4.pack(expand=True,fill="both")

    Heading_label = Label(Canvas4,text=" Search Employee-ID ",background="Grey",foreground="Red",font=('Courier',25))
    Heading_label.place(x=250,y=150)

    #input employee Phone number
    phone_label = Label(Canvas4,text=" Phone Number: ",font=("Helvetica", "18"))
    phone_label.config(background="#96bb7c")
    phone_label.place(x=200,y=300)

    phone_entry = Text(Canvas4,height=1,width=30,font=("Helvetica", "16"))
    phone_entry.place(x=400,y=300)

    #Search Button
    searchBtn = Button(Canvas4,text="Search Employee-ID",command=lambda:searchEmployee(phone_entry,Canvas4))
    searchBtn.place(x=250,y=450,width=150,height=50)

    #BAck Button
    BackBtn = Button(Canvas4,text="Back",command=lambda:Homepage(root,Canvas4))
    BackBtn.place(x=550,y=450,width=150,height=50)

    root.mainloop()

def searchEmployee(phone_entry,Canvas4):
    phonenum = phone_entry.get("1.0",END).strip()
    # print(phonenum)
    mydb = mysql.connector.connect(
        host="Localhost",
        user=user,
        password=mypass,
        database="Employee"
    )
    cursor = mydb.cursor()
    query = "SELECT Employeeid,Name FROM employeeData WHERE Phone = {}"
    cursor.execute(query.format(phonenum))
    result = cursor.fetchall()
    i = 0
    for x in result:
        progress = Label(Canvas4,text=("The Employee-ID Associated is::",x[0]," Name:",x[1]),font=('Courier',12))
        progress.place(x=125,y=525+i)
        i+=20



# root=Tk()
# searchData(root)