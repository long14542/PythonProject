from Database import *
class Values:
    def Validate(self, id, phone, email, wateramount):
        self.databse = Database()
        self. existId = self.databse.check_id_exist(id)
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif self.existId == "exist":
            return "existed id"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        elif not (wateramount.isdigit()):
            return "wateramount"
        else:
            return "SUCCESS"