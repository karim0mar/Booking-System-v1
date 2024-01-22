import json
import os
import time
from Classes.ClientData import ClientData, readData
from Classes.ReservationsData import ReservationsData
from Interface.CartControlInterface import CartControlInterface


def payPage():
    pass


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
              "\x1B[2;32m 2) Confirm & cancel a product\n"
              "\x1B[2;32m 3) Pay \n"
              "\x1B[2;32m 4) Exit \n")
        print("\x1B[3;31m Note! your max number of booking tickets is 5")
        operation = int(input("\n"))
        os.system("cls")
        match operation:
            case 0:
                payPage()
            case 1:
                if bookingData.getBookedTicketsNumber() < 5:
                    self.filmsPage()
                else:
                    print("You reached the maximum number of booking tickets")
                    self.reload()
            case 2:
                self.controlPage()
            case 3:
                pass
            case 4:
                exit(1)
            case _:
                print("Please Enter A Valid Option")
                self.reload()

    def filmsPage(self):
        print("\x1B[3;31m Enter 0 to back")
        data = readData("Films")
        bookingData = ReservationsData(self.email)
        filmID = 0
        BookedList = []
        for film in data["films"]:
            filmID = filmID + 1
            if film['filmName'] in bookingData.BookedTickets:
                Booked = "Booked"
                BookedList.append(filmID)
            else:
                Booked = ""
            print(
                f"\033[2;96mFilm number : {filmID}\n"
                f"Film Name : {film['filmName']} \x1B[3;31m{Booked}\n"
                f"\033[2;96mFilm Price : {film['filmPrice']}$\n"
                f"Film Date: {film['filmDate']}\n")
        operation = int(input("Book film number : "))
        os.system("cls")
        match operation:
            case 0:
                self.reload()
            case _:
                if operation <= filmID and operation not in BookedList:
                    self.bookFilmWithID(data["films"][operation - 1], self.email)
                else:
                    print("Please Enter A Valid Option")
                    time.sleep(0.3)
                    self.reload()

    def bookFilmWithID(self, filmData, email):
        bookingData = ReservationsData(self.email)
        bookingData.BookedTickets.append(filmData["filmName"])
        Payment = bookingData.TotalPayment
        jsonFile = open("Data/Reservations.json", "r+")
        data = json.load(jsonFile)
        index = 0
        for i in data["reservations"]:
            if i["email"] == email:
                i["BookedTickets"] = bookingData.BookedTickets
                del data["reservations"][index]
                data["reservations"].insert(index, i)
                break
            index = index + 1
        writeFile = open("Data/Reservations.json", "w")
        released = json.dumps(data, indent=4, separators=(',', ': '))
        writeFile.write(released)
        writeFile.close()
        self.filmsPage()

    def controlPage(self):
        CartControlInterface(self.email, self.password)
    def reload(self):
        time.sleep(0.6)
        os.system("cls")
        ClientInterface(self.email, self.password)
