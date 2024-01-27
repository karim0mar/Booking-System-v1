import os
import time

from Classes.AdminData import AdminData, checkAdminEmailExisted


def filmsPanel(email, password):
    print("1) Add film")
    print("2) Control films")
    print("0) Back")
    operation = int(input("\n->"))
    os.system("cls")
    match operation:
        case 0:
            adminPageUI(email, password)
        case 1:
            filmName = input("Enter film name: \n->")
            filmTime = input("Enter film time in minutes: \n->")
            filmYear = input("Enter film year: \n->")
            filmCategories = input("Enter film categories: ex. Comedy, Fantasy \n->")
            filmPrice = input("Enter film price: \n->")
            filmShowDate = input("Enter film ShowDate: ex. 2023-4-12 3:00 \n->")
            filmDescription = f"({filmYear}) {filmTime} min | {filmCategories}"
            from Classes.FilmsControl import addFilm
            if addFilm(email, filmName, filmDescription, filmPrice, filmShowDate):
                print("\nFilm added successfully.")
                os.system('cls')
                time.sleep(1)
                filmsPanel(email, password)
            else:
                print("Film already existed. Please try again.")
                time.sleep(1)
                os.system('cls')
                filmsPanel(email, password)
        case 2:
            from Interface.AdminFilmControl import AdminFilmControlInterface
            AdminFilmControlInterface(email, password)

        case _:
            print("Invalid Input")
            time.sleep(1.5)
            filmsPanel(email, password)


def clientPanel(email, password):
    print("1) Add Client")
    print("2) Remove Client")
    print("0) Back")
    operation = int(input("\n->"))
    os.system("cls")
    match operation:
        case 0:
            adminPageUI(email, password)
        case 1:
            from Interface.RegisterInterface import RegisterInterface
            registerData = RegisterInterface()
            registerData.register()
            if registerData.registerStatues:
                time.sleep(1)
                clientPanel(email, password)
        case 2:
            from Interface.AdminClientRemover import AdminClientRemover
            AdminClientRemover(email, password)


def transactions(email, password):
    from Classes.TransactionsClass import TransactionClass
    transactionsData = TransactionClass()
    transactionsData.showTransactions()
    print("Enter any key to back")
    operation = input("\n->")
    match operation:
        case _:
            os.system("cls")
            adminPageUI(email, password)


def adminPageUI(email, password):
    adminData = AdminData(email, password)
    if not checkAdminEmailExisted(email, password):
        exit(1)
    else:
        print(f"         Welcome to the admin control page {adminData.getName()} ..         \n")

        print("1) Films Panel")
        print("2) Client Panel")
        print("3) Show Transactions")
        print("4) Logout")
        operation = int(input("\n-> "))
        os.system("cls")
        match operation:
            case 1:
                filmsPanel(email, password)
            case 2:
                clientPanel(email, password)
            case 3:
                transactions(email, password)
            case 4:
                import main
                main.initialize()
            case _:
                print("Invalid Input")
                adminPageUI(email, password)

    pass
