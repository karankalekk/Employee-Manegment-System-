from tkinter import * 
from tkinter.ttk import *
from addData import *
from deleteData import *
from searchData import *
from exportData import *


def Homepage(root,canvas1=None):
    if(canvas1!=None):
        canvas1.destroy()
    root.title("Employee Data")
    Canvas2 = Canvas(root)
    Canvas2.config(bg="#11698e")
    Canvas2.pack(expand=True,fill="both")
    icon = PhotoImage(file="assets\icon.png")
    root.iconphoto(False,icon)
    HeadingLabel = Label(root,text=" Employee DataBase System ",font=('Courier',30))    
    HeadingLabel.config(background="grey",foreground="Black")
    HeadingLabel.place(x=175,y=100)

    s = Style()
    s.configure('my.TButton', font=('Helvetica', 11))
    AddDataBtn = Button(Canvas2,text=" ADD Employee ",style="my.TButton",command=lambda:addData(root,Canvas2))
    AddDataBtn.config(width=50)
    AddDataBtn.place(x=250,y=250,height=50)


    #Delete Btn
    deleteDataBtn = Button(Canvas2,text=" Delete Employee ",style="my.TButton",command=lambda:deleteData(root,Canvas2))
    deleteDataBtn.config(width=50)
    deleteDataBtn.place(x=250,y=325,height=50)

    #search id
    searchDataBtn = Button(Canvas2,text=" Search Employee-ID ",style="my.TButton",command=lambda:searchData(root,Canvas2))
    searchDataBtn.config(width=50)
    searchDataBtn.place(x=250,y=400,height=50)

    #Export 
    exportDataBtn = Button(Canvas2,text="Export  Data ",style="my.TButton",command=lambda:exportData(root,Canvas2))
    exportDataBtn.config(width=50)
    exportDataBtn.place(x=250,y=475,height=50)

    #Quit Button
    QuitBtn = Button(Canvas2,text=" Quit ",style="my.TButton",command=root.destroy)
    QuitBtn.config(width=50)
    QuitBtn.place(x=250,y=550,height=50)

    #name
    DevName = Label(Canvas2,text="Developed By: Rohit Kavitake(@_eighth_hocrux)")
    DevName.place(x=500,y=650)