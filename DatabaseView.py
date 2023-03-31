import tkinter
import tkinter.ttk
import tkinter.messagebox

class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        tkinter.Label(self.databaseViewWindow, text = "Database View Window",  width = 25).grid(pady = 5, column = 1, row = 1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady = 5, column = 1, row = 2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phone", "email",  "wateramount", "watercost")

        # Treeview column headings
        self.databaseView.heading("id", text = "ID")
        self.databaseView.heading("fName", text = "First Name")
        self.databaseView.heading("lName", text = "Last Name")
        self.databaseView.heading("dob", text = "D.O.B")
        self.databaseView.heading("mob", text = "M.O.B")
        self.databaseView.heading("yob", text = "Y.O.B")
        self.databaseView.heading("gender", text = "Gender")
        self.databaseView.heading("address", text = "Home Address")
        self.databaseView.heading("phone", text = "Phone Number")
        self.databaseView.heading("email", text = "Email ID")
        self.databaseView.heading("wateramount", text= "Amount of water (liter)")
        self.databaseView.heading("watercost", text= "Water cost (VND)")

        # Treeview columns
        self.databaseView.column("id", width = 40)
        self.databaseView.column("fName", width = 100)
        self.databaseView.column("lName", width = 100)
        self.databaseView.column("dob", width = 60)
        self.databaseView.column("mob", width = 60)
        self.databaseView.column("yob", width = 60)
        self.databaseView.column("gender", width = 60)
        self.databaseView.column("address", width = 200)
        self.databaseView.column("phone", width = 100)
        self.databaseView.column("email", width = 200)
        self.databaseView.column("wateramount", width=200)
        self.databaseView.column("watercost", width=200)


        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()