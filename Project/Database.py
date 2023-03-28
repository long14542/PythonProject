import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS client_info (id PRIMARYKEY text, fName text, lName text, dob text, mob text, yob text, gender text, address text, phone text, email text, waterclock text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email,waterclock):
        self.dbCursor.execute("INSERT INTO client_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, fName, lName, dob, mob, yob, gender, address, phone, email, waterclock))
        self.dbConnection.commit()

    def Update(self,  fName, lName, dob, mob, yob, gender, address, phone, email,waterclock,id):
        self.dbCursor.execute("UPDATE client_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, waterclock = ? WHERE id = ?", (fName, lName, dob, mob, yob, gender, address, phone, email, waterclock, id))
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