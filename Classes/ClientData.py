import json


def readData(fileName):
    file_path = f"Data/{fileName}.json"
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data


def checkEmailExisted(_email):
    data = readData("Clients")
    for i in data["clients"]:
        if i["email"] == _email:
            return True
    return False


class ClientData:
    def __init__(self, _email, _password):
        self.LoginStatues = False
        data = readData("Clients")

        for i in data["clients"]:
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
