from tkinter import *
from tkinter.ttk import *
import mysql.connector 
from config import *
# from addData import *

def deleteEmployee(Employeeid_entry,Canvas3):
    mydb = mysql.connector.connect(
        host="Localhost",
        user=user,
        password=mypass,
        database="Employee"
    )
    cursor = mydb.cursor()
    employeeid = (Employeeid_entry.get("1.0",END).strip())
    deletequery = "DELETE FROM EmployeeData WHERE Employeeid ={}; "
    cursor.execute(deletequery.format(employeeid))
    mydb.commit()
    progress = Label(Canvas3,text="Employee Details Deleted from Database")
    progress.place(x=200,y=525)
    progress.after(3000,progress.place_forget)
    print("Record deleted")


def deleteData(root,Canvas2=None):
    from home import Homepage
    if(Canvas2!=None):
        Canvas2.destroy()
    root.title("Employee Data - Delete Employee")
    root.geometry("900x700")
    icon = PhotoImage(file="assets\icon.png")
    root.iconphoto(False,icon)

    Canvas3 = Canvas(root)
    Canvas3.config(bg="#0d335d")
    Canvas3.pack(expand=True,fill="both")

    Heading_label = Label(Canvas3,text=" Delete Employee Data ",background="Grey",foreground="Red",font=('Courier',25))
    Heading_label.place(x=225,y=150)

    #input employeeid
    Employeeid_label = Label(Canvas3,text=" Employee ID: ",font=("Helvetica", "18"))
    Employeeid_label.config(background="#96bb7c")
    Employeeid_label.place(x=200,y=300)

    Employeeid_entry = Text(Canvas3,height=1,width=30,font=("Helvetica", "16"))
    Employeeid_entry.place(x=400,y=300)

    #Delete Button
    DeleteBtn = Button(Canvas3,text="Delete Data",command=lambda:deleteEmployee(Employeeid_entry,Canvas3))
    DeleteBtn.place(x=250,y=450,width=150,height=50)

    #BAck Button
    BackBtn = Button(Canvas3,text="Back",command=lambda:Homepage(root,Canvas3))
    BackBtn.place(x=550,y=450,width=150,height=50)

    root.mainloop()

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


    #Delete Btn
    deleteDataBtn = Button(Canvas2,text=" Delete Employee ",style="my.TButton",command=lambda:deleteData(root,Canvas2))
    deleteDataBtn.config(width=50)
    deleteDataBtn.place(x=250,y=400,height=50)

# root=Tk()
# deleteData(root)