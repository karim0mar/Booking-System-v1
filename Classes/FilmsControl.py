import os
import time

from Classes.AssistClass import writeData
from Classes.AssistClass import readData
from Classes.ReservationsData import ReservationsData

CURRENCY = "EGP"


def getFilmData():
    return readData("Films")["films"]


def getFilmDescription(filmName):
    for film in getFilmData():
        if filmName == film["filmName"]:
            return film["filmDescription"]
    return 0


def getFilmPrice(filmName):
    for film in getFilmData():
        if filmName == film["filmName"]:
            return film["filmPrice"]
    return 0


def getFilmDate(filmName):
    for film in getFilmData():
        if filmName == film["filmName"]:
            return film["filmDate"]
    return 0


def printFilmsData(filmsList):
    for film in filmsList:
        print(f"\033[1;95mFilm Name : {film}")
        print(f"Film Price : {getFilmPrice(film)}\x1B[2;32m {CURRENCY}")
        print(f"\033[1;95mFilm Date : {getFilmDate(film)}\n")


def bookingData(email):
    return ReservationsData(email)


def filmDataAfterChange(BookedTickets, email):
    data = readData("Reservations")
    index = 0
    for i in data["reservations"]:
        if i["email"] == email:
            i["BookedTickets"] = BookedTickets
            del data["reservations"][index]
            data["reservations"].insert(index, i)
            return data
        index = index + 1


class FilmsControl:

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password

    def showFilmsList(self):
        filmID = 0
        BookedList = []
        for film in getFilmData():
            filmID = filmID + 1
            filmName = film["filmName"]
            if filmName in bookingData(self.email).BookedTickets:
                Booked = "Booked"
                BookedList.append(filmID)
            else:
                Booked = ""
            print(
                f"\033[2;96mFilm number : {filmID}\n"
                f"Film Name : {filmName} \x1B[3;31m{Booked}\n"
                f"\033[2;96mFilm Description : {getFilmDescription(filmName)}\n"
                f"Film Price : {getFilmPrice(filmName)}$\n"
                f"Film Date: {getFilmDate(filmName)}\n")

        print("\x1B[3;31m Enter 0 to back")
        operation = int(input("\033[2;96mBook film number : \n->"))
        os.system("cls")
        match operation:
            case 0:
                return False
            case _:
                if operation <= filmID and operation not in BookedList:
                    if len(BookedList) <= 5:
                        self.bookFilmWithID(getFilmData()[operation - 1], self.email)
                    else:
                        print("You reached the maximum number of booking tickets")
                        time.sleep(3)
                        os.system("cls")
                        self.showFilmsList()
                else:
                    print("Please Enter A Valid Option")
                    time.sleep(3)
                    os.system("cls")
                    self.showFilmsList()

    def bookFilmWithID(self, filmData, email):
        bData = bookingData(email)
        bData.BookedTickets.append(filmData["filmName"])
        FilmData = filmDataAfterChange(bData.getBookedTickets(), email)
        writeData("Reservations", FilmData)
        os.system("cls")
        self.showFilmsList()

    def removeFilmWithName(self, filmData, email):
        try:
            bData = bookingData(email)
            bData.BookedTickets.remove(filmData)
            FilmData = filmDataAfterChange(bData.getBookedTickets(), email)
            writeData("Reservations", FilmData)
            from Interface.CartControlInterface import CartControlInterface
            os.system("cls")
            CartControlInterface(self.email, self.password).controlUI()
        except ValueError:
            print("Film name is not correct")
            time.sleep(0.4)