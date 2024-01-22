import json
import os
import time
from Classes.LoginClass import LoginClass
from Interface.ClientInterface import ClientInterface
from Interface.RegisterInterface import RegisterInterface


def register():
    file_path = "Data/Clients.json"
    file = open(file_path)
    data = json.load(file)
    data2 = {
        "email": "<EMAIL>",
    }
    data["clients"].append(data2)
    print(data["clients"])
    file2 = open(file_path, "w")
    json.dump(data, file2, indent=4, separators=(',', ': '))


def CLEAR():
    os.system("cls")


def LoginPage():
    username = input("Enter your email address:\n")
    password = input("Enter your password:\n")
    LoginProcess = LoginClass(username, password)
    if LoginProcess.login():
        print("Login successful")
        time.sleep(0.6)
        CLEAR()
        ClientInterface(username, password)
    else:
        print("Client not found.")
        time.sleep(0.5)
        CLEAR()
        init()


def RegisterPage():
    RegisterInterface()


def AdminPage():
    pass


def init():
    CLEAR()
    print("  \n\x1B[1;31m       Welcome To Booking Application  \n")

    operation = int(input("\x1B[2;32m"
                          "1) Login to booking system\n"
                          "2) Create an account\n\n"
                          "0) Admin Login\n"))
    CLEAR()
    match operation:
        case 1:
            LoginPage()
        case 2:
            RegisterPage()
        case 0:
            AdminPage()
        case _:
            print("Please Enter A Valid Option")
            exit(1)


if __name__ == '__main__':
    init()
