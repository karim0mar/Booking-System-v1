def checkEmailExisted(_email):
    from Classes.AssistClass import readData
    data = readData("Clients")
    for i in data["clients"]:
        if i["email"] == _email:
            return True
    return False


def getClientsData():
    from Classes.AssistClass import readData
    return readData("Clients")


def showClients():
    from Classes.ReservationsData import ReservationsData
    for client in getClientsData()["clients"]:
        clientsData = ClientData(client["email"], client["password"])
        reservationsData = ReservationsData(client["email"])
        print(f"\x1b[38;5;2mClient Name : {clientsData.getName()}")
        print(f"Client Email : {clientsData.getEmail()}")
        print(f"Client Password : {clientsData.getPassword()}")
        print(f"\x1b[38;5;2mPhone Number : {clientsData.getPhoneNumber()}")
        if reservationsData.ClientHasBooking:
            print(f"\x1b[38;5;2mNumber of booked sets : {reservationsData.getBookedTicketsNumber()}")
        print("----------------------------\n")


def removeClientWithEmail(_email):
    clientsData = getClientsData()
    for client in clientsData["clients"]:
        if client["email"] == _email:
            clientsData["clients"].remove(client)
            from Classes.AssistClass import writeData
            writeData("Clients", clientsData)
            return True

    return False


def ClientsNumber():
    return len(getClientsData()["clients"])


class ClientData:
    def __init__(self, _email, _password):
        self.LoginStatues = False
        from Classes.AssistClass import readData
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
