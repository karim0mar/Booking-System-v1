def checkAdminEmailExisted(_email, _password):
    from Classes.AssistClass import readData
    data = readData("Admins")
    for i in data["admins"]:
        if i["email"] == _email and i["password"] == _password:
            return True
    return False


class AdminData:
    def __init__(self, _email, _password):
        self.LoginStatues = False
        from Classes.AssistClass import readData
        data = readData("Admins")

        for i in data["admins"]:
            u = i["email"]
            p = i["password"]
            if u == _email and p == _password:
                self.email = _email
                self.password = _password
                self.name = i["name"]
                self.phoneNumber = i["phoneNumber"]
                self.LoginStatues = True
                break

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPhoneNumber(self):
        return self.phoneNumber

    def getPassword(self):
        return self.password
