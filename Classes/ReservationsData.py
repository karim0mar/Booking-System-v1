import json


class ReservationsData():
    def __init__(self, _email):
        ClientHasBooking = False
        file_path = "Data/Reservations.json"
        file = open(file_path)
        data = json.load(file)

        for i in data["reservations"]:
            u = i["email"]
            if u == _email:
                self.CustomerName = i["CustomerName"]
                self.BookedTickets = i["BookedTickets"]
                self.TotalPayment = i["TotalPayment"]
                self.BookingDate = i["BookingDate"]
                self.BookedTicketsNumber = len(i["BookedTickets"])
                ClientHasBooking = True
                break
            file.close()

    def getCustomerName(self):
        return self.CustomerName

    def getBookedTickets(self):
        return self.BookedTickets

    def getBookedTicketsNumber(self):
        return self.BookedTicketsNumber

    def getTotalPayment(self):
        return self.TotalPayment

    def getBookingDate(self):
        return self.BookingDate
