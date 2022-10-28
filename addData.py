
from tkinter import *
from tkinter.ttk import *
import mysql.connector
from config import *
import time
from deleteData import *



def addData(root,canvas2=None):
    from home import Homepage
    if(canvas2!=None):
        canvas2.destroy()
    # # root = Tk()
    # root.geometry("900x700")
    root.title("Employee Data - Add Employee")
    icon = PhotoImage(file="assets\icon.png")
    root.iconphoto(False,icon)
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#19d3da")
    # backadd = PhotoImage(file= "back-add.jpg")
    # Canvas1.config(background=backadd)
    Canvas1.pack(expand=True,fill=BOTH)

    HeadingLabel = Label(root,text=" ADD EMPLOYEE ",font=('Courier',25))
    HeadingLabel.config(background="grey",foreground="Black")
    HeadingLabel.place(x=330,y=100)

    #Employee name
    namelbl = Label(Canvas1,text=("Employee Name:"),font=("Helvetica", "18"))
    namelbl.config(background="#96bb7c")
    namelbl.place(x=175,y=200)

    name_entry = Text(Canvas1,height=1.5,width=40,font=("Helvetica", "12"))
    name_entry.place(x=430,y=200)

    #Employee Job Post
    joblbl = Label(Canvas1,text=("Job Post:"),font=("Helvetica", "18"))
    joblbl.config(background="#96bb7c")
    joblbl.place(x=175,y=250)

    post_entry = Text(Canvas1,height=1.5,width=40,font=("Helvetica", "12"))
    post_entry.place(x=430,y=250)

    #Employee Email
    Emaillbl = Label(Canvas1,text=("Employee Email:"),font=("Helvetica", "18"))
    Emaillbl.config(background="#96bb7c")
    Emaillbl.place(x=175,y=300)

    Email_entry = Text(Canvas1,height=1.5,width=40,font=("Helvetica", "12"))
    Email_entry.place(x=430,y=300)

    #Employee Phone
    phonelbl = Label(Canvas1,text=("Mobile number:"),font=("Helvetica", "18"))
    phonelbl.config(background="#96bb7c")
    phonelbl.place(x=175,y=350)

    phone_entry = Text(Canvas1,height=1.5,width=40,font=("Helvetica", "12"))
    phone_entry.place(x=430,y=350)
    
    #Employee Gender
    genderlbl = Label(Canvas1,text=("Gender:"),font=("Helvetica", "18"))
    genderlbl.config(background="#96bb7c")
    genderlbl.place(x=175,y=400)

    gender = StringVar()
    genderselect = Combobox(Canvas1,width=40,height=20,textvariable= gender)
    genderselect['values'] = ("MALE", "FEMALE", "CAN'T SAY")
    genderselect.place(x=430,y=400)
    genderselect.current()

    #employee Address
    addresslbl = Label(Canvas1,text=("Address:"),font=("Helvetica", "18"))
    addresslbl.config(background="#96bb7c")
    addresslbl.place(x=175,y=450)

    address_entry = Text(Canvas1,height=1.5,width=40,font=("Helvetica", "12"))
    address_entry.place(x=430,y=450)

    #submit button
    # helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
    SubmitBtn = Button(Canvas1,text="Submit Data",command= lambda:addEmployee(name_entry,Email_entry,address_entry,post_entry,phone_entry,gender,Canvas1))
    # SubmitBtn.grid(row=1, column=1, ipady=100, ipadx=10)
    SubmitBtn.config(width=30)
    SubmitBtn.place(x=200,y=550,height=50)

    #baack button
    BackBtn = Button(Canvas1,text="Back",command=lambda:Homepage(root,Canvas1))
    BackBtn.config(width=30)
    BackBtn.grid(ipady=100, ipadx=100)
    BackBtn.place(x=500,y=550,height=50)
    

    root.mainloop()

def addEmployee(name_entry,Email_entry,address_entry,post_entry,phone_entry,gender,Canvas1):
    name = name_entry.get("1.0",END).strip()
    post = post_entry.get("1.0",END).strip()
    phone = phone_entry.get("1.0",END).strip()
    email = Email_entry.get("1.0",END).strip()
    address = address_entry.get("1.0",END).strip()
    gender = gender.get()
    mydb = mysql.connector.connect(
    host="Localhost",
    user=user,
    password=mypass,
    database="Employee"
    )
    print(name,post,phone, email, address, gender)

    cursor = mydb.cursor()
    InsertingData = ("Insert into EmployeeData(Name, post, Gender, Email, Phone, Address) values(%s, %s, %s, %s, %s, %s)")
    values = (name, post, gender, email, phone, address)
    cursor.execute(InsertingData, values)
    mydb.commit()
    progress = Label(Canvas1,text="Employee Details Added to Database")
    progress.place(x=200,y=525)
    progress.after(3000,progress.place_forget)
        
# def Homepage(root,canvas1=None):
#     if(canvas1!=None):
#         canvas1.destroy()
#     root.title("Employee Data")
#     Canvas2 = Canvas(root)
#     Canvas2.config(bg="#11698e")
#     Canvas2.pack(expand=True,fill="both")
#     icon = PhotoImage(file="assets\icon.png")
#     root.iconphoto(False,icon)
#     HeadingLabel = Label(root,text=" Employee DataBase System ",font=('Courier',25))    
#     HeadingLabel.config(background="grey",foreground="Black")
#     HeadingLabel.place(x=200,y=100)

#     s = Style()
#     s.configure('my.TButton', font=('Helvetica', 11))
#     AddDataBtn = Button(Canvas2,text=" ADD Employee ",style="my.TButton",command=lambda:addData(root,Canvas2))
#     AddDataBtn.config(width=50)
#     AddDataBtn.place(x=250,y=300,height=50)


#     #Delete Btn
#     deleteDataBtn = Button(Canvas2,text=" Delete Employee ",style="my.TButton",command=lambda:deleteData(root,Canvas2))
#     deleteDataBtn.config(width=50)
#     deleteDataBtn.place(x=250,y=400,height=50,width=50)
# addData(root)