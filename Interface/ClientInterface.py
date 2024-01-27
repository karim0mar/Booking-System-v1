import os
import time

from Classes.ClientData import ClientData
from Classes.FilmsControl import FilmsControl
from Classes.ReservationsData import ReservationsData
from Interface.CartControlInterface import CartControlInterface


class ClientInterface:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password
        self.clientUI()

    def clientUI(self):
        LoginData = ClientData(self.email, self.password)
        bookingData = ReservationsData(self.email)
        print(f"\x1B[2;36m Welcome {LoginData.getName()}\n your Cart Items are: {bookingData.BookedTicketsNumber}\n")
        print("\x1B[2;32m 1) Add films to cart\n"
              "\x1B[2;32m 2) Confirm or Cancel your products\n"
              "\x1B[2;32m 3) Logout \n")
        print("\x1B[3;31m Note! your max number of booking tickets is 5")
        operation = int(input("\n->"))
        os.system("cls")
        match operation:
            case 1:
                if bookingData.getBookedTicketsNumber() < 5:
                    self.filmsPage()
                else:
                    print("You reached the maximum number of booking tickets")
                    self.reload()
            case 2:
                self.controlPage()
            case 3:
                import main
                main.initialize()
            case _:
                print("Please Enter A Valid Option")
                self.reload()

    def filmsPage(self):
        if not FilmsControl(self.email, self.password).showFilmsList():
            self.reload()

    def controlPage(self):
        if not CartControlInterface(self.email, self.password).controlUI():
            self.reload()

    def reload(self):
        time.sleep(0.2)
        os.system("cls")
        ClientInterface(self.email, self.password)
