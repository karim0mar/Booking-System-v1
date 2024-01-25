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
        print(f"\x1b[38;5;2mFilm Name : {film}")
        print(f"Ticket Price : {getFilmPrice(film)}\x1B[2;32m {CURRENCY}")
        print(f"\x1b[38;5;2mFilm Date : {getFilmDate(film)}\n")


def editFilmPrice(filmName, newPrice):
    filmData = readData("Films")
    index = 0
    for film in filmData["films"]:
        if filmName == film["filmName"]:
            film["filmPrice"] = newPrice
            del filmData["films"][index]
            filmData["films"].insert(index, film)
            writeData("Films", filmData)
            break
        index = index + 1


def bookingData(email):
    return ReservationsData(email)


def filmDataAfterChange(BookedTickets, email, password):
    data = readData("Reservations")
    index = 0
    from Classes.PayClass import PayClass
    payClass = PayClass(email, password, BookedTickets)
    for i in data["reservations"]:
        if i["email"] == email:
            i["BookedTickets"] = BookedTickets
            i["TotalPayment"] = payClass.getTotalPayment()
            del data["reservations"][index]
            data["reservations"].insert(index, i)
            return data
        index = index + 1


def checkFilmExisted(filmName):
    for film in getFilmData():
        if filmName == film["filmName"]:
            return True
    return False


def addFilm(adminEmail, filmName, filmDescription, filmPrice, filmDate):
    if not checkFilmExisted(filmName):
        filmData = {
            "filmName": filmName,
            "filmDescription": filmDescription,
            "filmPrice": filmPrice,
            "filmDate": filmDate,
            "addedBy": adminEmail
        }
        filmsFileName = "Films"
        filmsData = readData(filmsFileName)
        filmsData["films"].append(filmData)
        writeData(filmsFileName, filmsData)
        return True
    else:
        return False


def removeFilmWithName(filmName):
    if checkFilmExisted(filmName):
        bData = readData("Films")
        for filmData in bData["films"]:
            if filmData["filmName"] == filmName:
                bData["films"].remove(filmData)
                writeData("Films", bData)
                return True
        print("Film name is not correct")
        time.sleep(1)
        return False


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
                f"Ticket Price : {getFilmPrice(filmName)}$\n"
                f"Film Date: {getFilmDate(filmName)}\n")

        print("\x1B[3;31m Enter 0 to back")
        operation = int(input("\033[2;96mBook film number : \n->"))
        os.system("cls")
        match operation:
            case 0:
                return False
            case _:
                if 0 <= operation <= filmID and operation not in BookedList:
                    if len(BookedList) < 5:
                        print(len(BookedList))
                        self.bookFilmWithID(getFilmData()[operation - 1], self.email)
                    else:
                        print("You reached the maximum number of booking tickets")
                        time.sleep(1.5)
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
        FilmData = filmDataAfterChange(bData.getBookedTickets(), self.email, self.password)
        writeData("Reservations", FilmData)
        os.system("cls")
        self.showFilmsList()

    def removeClientFilmWithName(self, filmName):
        try:
            if checkFilmExisted(filmName):
                bData = bookingData(self.email)
                bData.BookedTickets.remove(filmName)
                FilmData = filmDataAfterChange(bData.getBookedTickets(), self.email, self.password)
                writeData("Reservations", FilmData)
                return True
        except ValueError:
            print("Film name is not correct")
            time.sleep(0.4)
            return False
