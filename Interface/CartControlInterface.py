import os
import time

from Classes.FilmsControl import FilmsControl
from Classes.ReservationsData import ReservationsData


class CartControlInterface:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password
        self.controlUI()

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
            filmControl = FilmsControl(filmsList)
            filmControl.printFilmsData()
            print("\x1B[3;31m Enter 0 to back")

        else:
            print("\x1B[3;31m Your cart is empty")
            time.sleep(1.2)
            os.system("cls")
            from Interface.ClientInterface import ClientInterface
            ClientInterface(self.email, self.password)
