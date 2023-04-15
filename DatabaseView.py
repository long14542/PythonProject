import tkinter
import tkinter.ttk
import tkinter.messagebox

class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        self.databaseViewWindow.wm_title("Database View")
        self.databaseViewWindow.geometry("1100x170+120+340")
        self.databaseViewWindow.iconbitmap("D:\B2\PythonProject\icon\SearchIcon.ico")
        # Label widgets
        tkinter.Label(self.databaseViewWindow, text = "Database View Window",  width = 25).pack(side="top", fill="x")

        self.scrollbarx = tkinter.Scrollbar(self.databaseViewWindow, orient="horizontal")
        self.scrollbary = tkinter.Scrollbar(self.databaseViewWindow, orient="vertical")
        self.scrollbarx.pack(side="bottom", fill="x", )
        self.scrollbary.pack(side="right", fill="y", )


        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow, xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set, selectmode="extended")
        self.databaseView.pack(fill="both",expand=1)

        self.scrollbarx.config(command=self.databaseView.xview)
        self.scrollbary.config(command=self.databaseView.yview)
        
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "Name", "dob", "gender", "address", "phone", "email", "billperiod",  "wateramount", "charges")

        # Treeview column headings
        self.databaseView.heading("id", text = "ID")
        self.databaseView.heading("Name", text = "Name")
        self.databaseView.heading("dob", text = "DOB")
        self.databaseView.heading("gender", text = "Gender")
        self.databaseView.heading("address", text = "Home Address")
        self.databaseView.heading("phone", text = "Phone Number")
        self.databaseView.heading("email", text = "Email ID")
        self.databaseView.heading("billperiod", text = "Bill period")
        self.databaseView.heading("wateramount", text= "Amount of water (liter)")
        self.databaseView.heading("charges", text= "Charges")

        # Treeview columns
        self.databaseView.column("id",anchor= "center", width = 40)
        self.databaseView.column("Name",anchor= "center", width = 200)
        self.databaseView.column("dob",anchor= "center", width = 120)
        self.databaseView.column("gender", anchor= "center",width = 60)
        self.databaseView.column("address",anchor= "center", width = 200)
        self.databaseView.column("phone",anchor= "center", width = 100)
        self.databaseView.column("email", anchor= "center",width = 200)
        self.databaseView.column("billperiod",anchor= "center", width = 200)
        self.databaseView.column("wateramount",anchor= "center", width=200)
        self.databaseView.column("charges",anchor= "center", width=200)


        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()