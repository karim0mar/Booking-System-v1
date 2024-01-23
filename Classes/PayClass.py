from Classes.AssistClass import writeData, readData
from Classes.ClientData import ClientData
from Classes.FilmsControl import getFilmPrice, filmDataAfterChange
from Classes.ReservationsData import ReservationsData


class PayClass:

    def __init__(self, _email, _password, _filmList):
        self.email = _email
        self.password = _password
        self.filmList = _filmList

    def getTotalPayment(self):
        totalPayment = 0
        for film in self.filmList:
            totalPayment += getFilmPrice(film)
        return totalPayment

    def confirmPayment(self):
        try:
            bData = ReservationsData(self.email)
            bData.BookedTickets = []
            FilmData = filmDataAfterChange(bData.getBookedTickets(), self.email)
            writeData("Reservations", FilmData)
            self.sendPaymentReport()
            return True
        except ValueError:
            return False

    def sendPaymentReport(self):
        import time
        customerData = ClientData(self.email, self.password)
        transaction = {
            "CustomerName": customerData.getName(),
            "CustomerEmail": self.email,
            "BookedTickets": self.filmList,
            "TotalPayment": self.getTotalPayment(),
            "BookingDate": time.strftime("%d/%m/%Y", time.localtime())
        }
        transactionsFileName = "Transactions"
        transactionsData = readData(transactionsFileName)
        transactionsData["successful_transactions"].append(transaction)
        writeData(transactionsFileName, transactionsData)
