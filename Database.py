import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS client_info (id PRIMARYKEY text, fName text, lName text, dob text, mob text, yob text, gender text, address text, phone text, email text, wateramount float, watercost float)")
        self.dbCursor.execute("UPDATE client_info SET watercost = 5.973*wateramount WHERE wateramount >= 0.00 and wateramount <10")
        self.dbCursor.execute("UPDATE client_info SET watercost = 10.00*5.973+ (wateramount-10.00)*7.052 WHERE wateramount >= 10.00 and wateramount <20")
        self.dbCursor.execute("UPDATE client_info SET watercost = 10.00*5.973+ 10.00*7.052 +(wateramount-20.00)*8.669 WHERE wateramount >= 20.00 and wateramount <30")
        self.dbCursor.execute("UPDATE client_info SET watercost = 10.00*5.973+10.00*7.052+10.00*8.669+(wateramount-30.00)*15.929 WHERE 30.00<=wateramount")
        self.dbConnection.commit()
        
    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, wateramount, watercost= 2.5):
        self.dbCursor.execute("INSERT INTO client_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(id, fName, lName, dob, mob, yob, gender, address, phone, email, float(wateramount), float(watercost)))        
        self.dbConnection.commit()

    def Update(self, fName, lName, dob, mob, yob, gender, address, phone, email,wateramount,id):
        self.dbCursor.execute("UPDATE client_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, wateramount = ? WHERE id = ?", (fName, lName, dob, mob, yob, gender, address, phone, email, wateramount, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM client_info WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
    
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM client_info WHERE id = ?", (id, ))
        self.dbConnection.commit()

    def Display(self):  
        self.dbCursor.execute("SELECT * FROM client_info")
        records = self.dbCursor.fetchall()
        return records
    
