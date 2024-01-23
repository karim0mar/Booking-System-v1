import json

from Classes.AssistClass import readData


class ReservationsData:
    def __init__(self, _email):
        self.ClientHasBooking = False
        self.data = readData("Reservations")
        for i in self.data["reservations"]:
            u = i["email"]
            if u == _email:
                self.CustomerName = i["CustomerName"]
                self.BookedTickets = i["BookedTickets"]
                self.TotalPayment = i["TotalPayment"]
                self.BookingDate = i["BookingDate"]
                self.BookedTicketsNumber = len(i["BookedTickets"])
                self.ClientHasBooking = True
                break

    def getFileData(self):
        return self.data

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

    def getClientHasBooking(self):
        return self.ClientHasBooking
