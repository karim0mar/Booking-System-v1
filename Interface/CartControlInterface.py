import os
import time

from Classes.FilmsControl import printFilmsData, FilmsControl
from Classes.ReservationsData import ReservationsData


def confirmPayment(email, password):
    pass


class CartControlInterface:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password

    def controlUI(self):
        print("\x1B[3;33m          Welcome to the control page ..         \n")
        film_counter = 0
        filmsList = []
        bookingData = ReservationsData(self.email)
        for reservation in bookingData.getFileData()["reservations"]:
            if reservation["email"] == self.email:
                for film in reservation["BookedTickets"]:
                    film_counter += 1
                    filmsList.append(film)
                break
        if len(filmsList) > 0:
            printFilmsData(filmsList)
            print("\x1B[3;31m Enter 0 to back")
            operation = input("\x1B[3;33m"
                              " yes to confirm \n rem (Film Name) to remove a film \n->")
            match operation:
                case "yes", "YES":
                    confirmPayment(email=self.email, password=self)
                case "0":
                    return False
                case _:
                    if "rem" in operation:
                        filmName = operation.split("rem ")
                        filmControl = FilmsControl(self.email, self.password)
                        filmControl.removeFilmWithName(filmName[1], email=self.email)

                    else:
                        return False

        else:
            print("\x1B[3;31m Your cart is empty")
            time.sleep(1.2)
            os.system("cls")
            from Interface.ClientInterface import ClientInterface
            ClientInterface(self.email, self.password)
