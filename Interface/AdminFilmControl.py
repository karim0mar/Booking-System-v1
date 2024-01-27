import os
import time

from Classes.FilmsControl import removeFilmWithName, editFilmPrice, checkFilmExisted
from Interface.AdminInterface import filmsPanel


def AdminFilmControlInterface(email, password):
    from Classes.FilmsControl import printFilmsData
    from Classes.FilmsControl import getFilmData
    filmData = []
    for film in getFilmData():
        filmData.append(film["filmName"])
    printFilmsData(filmData)
    print("\x1b[48;2;255;0;0m Enter 0 to back")
    operation = input("\033[0m\x1B[3;33m "
                      "price (Film Name) to (New Price) \n "
                      "rem (Film Name) to remove a film \n"
                      "\x1B[3;31m "
                      "Note! rem * removes all films \n"
                      " \n->")
    match operation:
        case "0":
            filmsPanel(email, password)
        case _:

            if "rem" in operation:
                filmName = operation.split("rem ")
                if filmName[1] == '*':
                    for film in filmData:
                        removeFilmWithName(film)
                    os.system("cls")
                    filmsPanel(email, password)
                else:
                    removeFilmWithName(filmName[1])
                    AdminFilmControlInterface(email, password)
            elif "price" in operation:
                try:
                    _input = operation[6:].split(" to ")
                    filmName = _input[0]
                    if checkFilmExisted(filmName):
                        filmPrice = float(_input[1])
                        editFilmPrice(filmName, filmPrice)
                        AdminFilmControlInterface(email, password)
                    else:
                        print("No film with that name exists")
                        time.sleep(2)
                        os.system("cls")
                        AdminFilmControlInterface(email, password)
                except ValueError:
                    print("Invalid input")
                    time.sleep(2)
                    os.system("cls")
                    AdminFilmControlInterface(email, password)
            else:
                pass
