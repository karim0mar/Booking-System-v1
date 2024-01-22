import json

from Classes.ClientData import ClientData, readData


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
    writeClient = open(f"Data/{clientFileName}.json", "w")
    json.dump(clientData, writeClient, indent=4, separators=(',', ': '))
    writeClient.close()
    writeReservation = open(f"Data/{reservationFileName}.json", "w")
    json.dump(reservationData, writeReservation, indent=4, separators=(',', ': '))
    writeReservation.close()
    return True


class RegisterClass:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password
