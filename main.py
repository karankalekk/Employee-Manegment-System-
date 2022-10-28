
#modules needed
from tkinter import * 
import mysql.connector
from config import *
from tkinter.ttk import *
# from addData import *

# from deleteData import deleteData,deleteEmployee
from home import *

global root



if __name__ == "__main__":
    root = Tk()
    root.geometry("900x700")
    startup()
    Homepage(root)
    root.mainloop()