import tkinter
import tkinter.ttk
import tkinter.messagebox
from Database import *

class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")

        # Initializing all the variables
        self.id = id

        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.wateramount = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.yearList = list(range(1900, 2024))

        # Labels
        tkinter.Label(self.window, text = "client ID",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = id,  width = 25).grid(pady = 5, column = 3, row = 1)
        tkinter.Label(self.window, text = "First Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Last Name",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "D.O.B",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "M.O.B",  width = 25).grid(pady = 5, column = 1, row = 5)
        tkinter.Label(self.window, text = "Y.O.B",  width = 25).grid(pady = 5, column = 1, row = 6)
        tkinter.Label(self.window, text = "Gender",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Home Address",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Phone Number",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Email ID",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Amount of water", width = 25).grid(pady = 5, column = 1, row = 11)
        # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id)
        
        tkinter.Label(self.window, text = self.searchResults[0][1],  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.window, text = self.searchResults[0][2],  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.window, text = self.searchResults[0][3],  width = 25).grid(pady = 5, column = 2, row = 4)
        tkinter.Label(self.window, text = self.searchResults[0][4],  width = 25).grid(pady = 5, column = 2, row = 5)
        tkinter.Label(self.window, text = self.searchResults[0][5],  width = 25).grid(pady = 5, column = 2, row = 6)
        tkinter.Label(self.window, text = self.searchResults[0][6],  width = 25).grid(pady = 5, column = 2, row = 7)
        tkinter.Label(self.window, text = self.searchResults[0][7],  width = 25).grid(pady = 5, column = 2, row = 8)
        tkinter.Label(self.window, text = self.searchResults[0][8],  width = 25).grid(pady = 5, column = 2, row = 9)
        tkinter.Label(self.window, text = self.searchResults[0][9],  width = 25).grid(pady = 5, column = 2, row = 10)
        tkinter.Label(self.window, text = self.searchResults[0][10],  width = 25).grid(pady = 5, column = 2, row = 11)

        # Fields
        # Entry widgets
        self.fNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fName)
        self.lNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lName)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.email)
        self.wateramountEntry = tkinter.Entry(self.window, width = 25, textvariable = self.wateramount)

        self.fNameEntry.grid(pady = 5, column = 3, row = 2)
        self.lNameEntry.grid(pady = 5, column = 3, row = 3)
        self.addressEntry.grid(pady = 5, column = 3, row = 8)
        self.phoneEntry.grid(pady = 5, column = 3, row = 9)
        self.emailEntry.grid(pady = 5, column = 3, row = 10)
        self.wateramountEntry.grid(pady = 5, column = 3, row = 11)
        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList, width = 20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, width = 20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList, width = 20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values = self.genderList, width = 20)

        self.dobBox.grid(pady = 5, column = 3, row = 4)
        self.mobBox.grid(pady = 5, column = 3, row = 5)
        self.yobBox.grid(pady = 5, column = 3, row = 6)
        self.genderBox.grid(pady = 5, column = 3, row = 7)

        # Button widgets
        tkinter.Button(self.window, width = 20, text = "Update", command = self.Update).grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Reset", command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Close", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)

        self.window.mainloop()

    def Update(self):
        self.database = Database()
        self.database.Update(self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.wateramountEntry.get(), self.id)
        tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

    def Reset(self):
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.wateramountEntry.delete(0, tkinter.END)