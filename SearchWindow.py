import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from Database import Database
from DatabaseView import DatabaseView

class SearchDeleteWindow:
    def __init__(self, task):
        window = tk.Tk()
        window.wm_title(task + " data")

        self.id = tk.StringVar()
        self.fName = tk.StringVar()
        self.lName = tk.StringVar()
        self.heading = "Please enter client ID to " + task

        tk.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tk.Label(window, text="client ID", width=10).grid(pady=5, row=2)

        self.idEntry = tk.Entry(window, width=5, textvariable=self.id)
        self.idEntry.grid(pady=5, row=3)

        if task == "Search":
            tk.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
        elif task == "Delete":
            tk.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())
