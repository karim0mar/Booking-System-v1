from Classes.AssistClass import readData, writeData


def registerEmail(email, password, fullName, phoneNumber):
    clientFileName = "Clients"
    clientData = readData(clientFileName)
    reservationFileName = "Reservations"
    reservationData = readData(reservationFileName)
    client = {
        "email": email,
        "password": password,
        "name": fullName,
        "phoneNumber": phoneNumber,
        "accountType": "usr"
    }
    reservation = {
        "CustomerName": fullName,
        "email": email,
        "BookedTickets": [],
        "TotalPayment": 0.0,
        "BookingDate": None
    }
    clientData["clients"].append(client)
    reservationData["reservations"].append(reservation)
    writeData(clientFileName, clientData)
    writeData(reservationFileName, reservationData)
    return True


class RegisterClass:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password
