import tkinter
import tkinter.ttk
import tkinter.messagebox
from Database import *
from DatabaseView import *


class SearchWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Search data")
        self.window.geometry("500x200+240+100")
        self.window.iconbitmap("D:\B2\PythonProject\icon\SearchIcon.ico")
        self.window.wm_resizable(False,False)

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.heading = "Please enter client ID to search " 

        # Labels
        tkinter.Label(self.window, text = self.heading, width = 50).grid(pady = 20, row = 1)
        tkinter.Label(self.window, text = "client ID", width = 10).grid(pady = 5,column=0, row = 2)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.window, width = 5, textvariable = self.id)
        self.idEntry.grid(pady = 5, row = 3)

        # Button widgets
        tkinter.Button(self.window, width = 10, text = "Search", command = self.Search).place(x=280, y=150)
        tkinter.Button(self.window, width = 10, text = "Close", command = self.window.destroy).place(x=370, y=150)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search2(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)
    
        