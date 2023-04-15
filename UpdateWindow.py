import tkinter
import tkinter.ttk
import tkinter.messagebox
from Database import *
from HomPage import *

class UpdateWindow:
    def __init__(self, iid, callback):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")

        self.callback = callback
        # Initializing all the variables
        self.row = iid
        self.id = self.row[0]
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.wateramount = tkinter.StringVar() 

        self.genderList = ["Male", "Female", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = list(range(1, 13))
        self.yearList = list(range(1900, 2024))

        # Labels
        tkinter.Label(self.window, text = "client ID",  width = 25).grid(pady = 5, column = 1, row = 1)
        tkinter.Label(self.window, text = self.id,  width = 25).grid(pady = 5, column = 2, row = 1)
        tkinter.Label(self.window, text = "First Name",  width = 25).grid(pady = 5, column = 1, row = 2)
        tkinter.Label(self.window, text = "Last Name",  width = 25).grid(pady = 5, column = 1, row = 3)
        tkinter.Label(self.window, text = "DOB",  width = 25).grid(pady = 5, column = 1, row = 4)
        tkinter.Label(self.window, text = "Gender",  width = 25).grid(pady = 5, column = 1, row = 7)
        tkinter.Label(self.window, text = "Home Address",  width = 25).grid(pady = 5, column = 1, row = 8)
        tkinter.Label(self.window, text = "Phone Number",  width = 25).grid(pady = 5, column = 1, row = 9)
        tkinter.Label(self.window, text = "Email",  width = 25).grid(pady = 5, column = 1, row = 10)
        tkinter.Label(self.window, text = "Bill period from",  width = 25).grid(pady = 5, column = 1, row = 11)
        tkinter.Label(self.window, text = "Bill period to",  width = 25).grid(pady = 5, column = 1, row = 12)
        tkinter.Label(self.window, text = "Amount of water", width = 25).grid(pady = 5, column = 1, row = 13)

        # Fields
        # Entry widgets
        self.fNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fName)
        self.lNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lName)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.email)
        self.wateramountEntry = tkinter.Entry(self.window, width = 25, textvariable = self.wateramount)

        self.fNameEntry.grid(pady = 5, column = 2, row = 2)
        self.lNameEntry.grid(pady = 5, column = 2, row = 3)
        self.addressEntry.grid(pady = 5, column = 2, row = 8)
        self.phoneEntry.grid(pady = 5, column = 2, row = 9)
        self.emailEntry.grid(pady = 5, column = 2, row = 10)
        self.wateramountEntry.grid(pady = 5, column = 2, row = 13)
       
        # Combobox widgets
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, )
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList)
        self.billperiodfrom_dateBox = tkinter.ttk.Combobox(self.window, values= self.dateList )
        self.billperiodfrom_monthBox = tkinter.ttk.Combobox(self.window, values= self.monthList )
        self.billperiodfrom_yearBox = tkinter.ttk.Combobox(self.window, values= self.yearList )
        self.billperiodto_dateBox = tkinter.ttk.Combobox(self.window, values= self.dateList )
        self.billperiodto_monthBox = tkinter.ttk.Combobox(self.window, values= self.monthList )
        self.billperiodto_yearBox = tkinter.ttk.Combobox(self.window, values= self.yearList )        
        self.genderBox = tkinter.ttk.Combobox(self.window, values = self.genderList, width = 20)

        self.dobBox.place(y = 100, x=200, width=46, height=19)
        self.mobBox.place(y = 100, x=248, width=45, height=19)
        self.yobBox.place(y = 100, x=295, width=48, height=19)
        self.billperiodfrom_dateBox.place(y = 254, x=200, width=46, height=19)
        self.billperiodfrom_monthBox.place(y = 254, x=248, width=45, height=19)       
        self.billperiodfrom_yearBox.place(y = 254, x=295, width=48, height=19)       
        self.billperiodto_dateBox.place(y = 283, x=200, width=46, height=19)       
        self.billperiodto_monthBox.place(y = 283, x=248, width=45, height=19)       
        self.billperiodto_yearBox.place(y = 283, x=295, width=48, height=19)       
        self.genderBox.grid(pady = 5, column = 2, row = 7)

        self.database = Database()
        self.olddata = self.database.Search(self.id)

        #inser old data
        self.fNameEntry.insert(0, self.olddata[0][1])
        self.lNameEntry.insert(0, self.olddata[0][2])
        self.dobBox.insert(0,self.olddata[0][3])
        self.mobBox.insert(0, self.olddata[0][4])
        self.yobBox.insert(0, self.olddata[0][5])
        self.genderBox.insert(0,self.olddata[0][6])
        self.addressEntry.insert(0,self.olddata[0][7])
        self.phoneEntry.insert(0, self.olddata[0][8])
        self.emailEntry.insert(0, self.olddata[0][9])
        self.billperiodfrom_dateBox.insert(0, self.olddata[0][10])
        self.billperiodfrom_monthBox.insert(0, self.olddata[0][11])
        self.billperiodfrom_yearBox.insert(0, self.olddata[0][12])
        self.billperiodto_dateBox.insert(0, self.olddata[0][13])
        self.billperiodto_monthBox.insert(0, self.olddata[0][14])
        self.billperiodto_yearBox.insert(0, self.olddata[0][15])       
        self.wateramountEntry.insert(0, self.olddata[0][16])

        # Button widgets
        tkinter.Button(self.window, width = 20, text = "Update", command = self.Update).grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Reset", command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Close", command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)
        
        self.window.mainloop()


    def Update(self):
        self.database = Database()
        self.database.Update(self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.billperiodfrom_dateBox.get(), self.billperiodfrom_monthBox.get(), self.billperiodfrom_yearBox.get() ,self.billperiodto_dateBox.get(), self.billperiodto_monthBox.get(), self.billperiodto_yearBox.get() ,self.wateramountEntry.get(), self.id)
        self.d = self.database.Display()
        self.e = self.database.Search2(self.id)
        self.callback(self.d, self.e)
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
        self.billperiodfrom_dateBox.delete(0, tkinter.END)
        self.billperiodfrom_monthBox.delete(0, tkinter.END)
        self.billperiodfrom_yearBox.delete(0, tkinter.END)
        self.billperiodto_dateBox.delete(0, tkinter.END)
        self.billperiodto_monthBox.delete(0, tkinter.END)
        self.billperiodto_yearBox.delete(0, tkinter.END)
        self.wateramountEntry.delete(0, tkinter.END)