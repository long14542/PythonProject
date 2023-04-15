import sqlite3

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS client_info (id PRIMARYKEY text, fName text, lName text, dob text, mob text, yob text, gender text, address text, phone text, email text, billperiodfrom_date text, billperiodfrom_month text, billperiodfrom_year text, billperiodto_date text, billperiodto_month text, billperiodto_year text, wateramount real, charges real)")        
        self.calculate_watercharges()
        self.dbConnection.commit()

    def calculate_watercharges(self):
        self.dbCursor.execute("UPDATE client_info SET charges = 5.973*wateramount WHERE wateramount >= 0.00 and wateramount <10")
        self.dbCursor.execute("UPDATE client_info SET charges = 10.00*5.973+ (wateramount-10.00)*7.052 WHERE wateramount >= 10.00 and wateramount <20")
        self.dbCursor.execute("UPDATE client_info SET charges = 10.00*5.973+ 10.00*7.052 +(wateramount-20.00)*8.669 WHERE wateramount >= 20.00 and wateramount <30")
        self.dbCursor.execute("UPDATE client_info SET charges = 10.00*5.973+10.00*7.052+10.00*8.669+(wateramount-30.00)*15.929 WHERE 30.00<=wateramount")
        self.dbConnection.commit()
    
    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, billperiodfrom_date, billperiodfrom_month, billperiodfrom_year, billperiodto_date,billperiodto_month, billperiodto_year, wateramount, charges= 94.99):
        self.dbCursor.execute("INSERT INTO client_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?)",(id, fName, lName, dob, mob, yob, gender, address, phone, email, billperiodfrom_date,billperiodfrom_month, billperiodfrom_year , billperiodto_date, billperiodto_month,billperiodto_year ,wateramount, charges))        
        self.calculate_watercharges()
        self.dbConnection.commit()

    def Update(self, fName, lName, dob, mob, yob, gender, address, phone, email, billperiodfrom_date,billperiodfrom_month, billperiodfrom_year, billperiodto_date, billperiodto_month, billperiodto_year, wateramount,id):
        self.dbCursor.execute("UPDATE client_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phone = ?, email = ?, billperiodfrom_date = ? , billperiodfrom_month = ? ,billperiodfrom_year = ? ,billperiodto_date = ?, billperiodto_month = ?,billperiodto_year = ?, wateramount = ? WHERE id = ?", (fName, lName, dob, mob, yob, gender, address, phone, email, billperiodfrom_date, billperiodfrom_month,billperiodfrom_year ,billperiodto_date,billperiodto_month, billperiodto_year ,wateramount, id))
        self.calculate_watercharges()
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT id,fName,lName,dob,mob ,yob, gender, address, phone, email, billperiodfrom_date, billperiodfrom_month, billperiodfrom_year,billperiodto_date, billperiodto_month, billperiodto_year, wateramount FROM client_info WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
    
    def Search2(self, id):
        self.dbCursor.execute("SELECT id,lName || ' ' || fName  AS Name, dob || '-' || mob || '-' || yob AS DOB, gender, address, phone, email, billperiodfrom_date|| '/' || billperiodfrom_month || '/' || billperiodfrom_year || ' - ' || billperiodto_date || '/' || billperiodto_month || '/' || billperiodto_year AS billperiod, wateramount, charges FROM client_info WHERE id = ?", (id, ))
        searchResults = self.dbCursor.fetchall()
        return searchResults
    
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM client_info WHERE id = ?", (id, ))
        self.dbConnection.commit()
    
    def Display(self):  
        self.calculate_watercharges()
        self.dbCursor.execute("SELECT id,lName || ' ' || fName  AS Name, dob || '-' || mob || '-' || yob AS DOB, gender, address, phone, email, billperiodfrom_date|| '/' || billperiodfrom_month || '/' || billperiodfrom_year || ' - ' || billperiodto_date || '/' || billperiodto_month || '/' || billperiodto_year AS billperiod, wateramount, charges FROM client_info")
        self.dbConnection.commit()
        records = self.dbCursor.fetchall()
        return records
    
