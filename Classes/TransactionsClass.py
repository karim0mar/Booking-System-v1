from Classes.AssistClass import readData


class TransactionClass:
    def __init__(self):
        self.data = None
        self.getTransactionsData()

    def showTransactions(self):
        for i in self.data:
            c = i["CustomerName"]
            e = i["CustomerEmail"]
            b = i["BookedTickets"]
            t = i["TotalPayment"]
            d = i["BookingDate"]
            print(f"\x1b[38;5;2mCustomer Name : {c}")
            print(f"\x1b[38;5;2mCustomer Email : {e}")
            print(f"\x1b[38;5;2mBooked Tickets : {b}")
            print(f"\x1b[38;5;2mTotal Payment : {t}")
            print(f"\x1b[38;5;2mBooking Date : {d}")
            print('\n')

    def getTransactionsData(self):
        self.data = readData("Transactions")["successful_transactions"]
