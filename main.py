import os
import sys


def CLEAR():
    os.system("cls")


def LoginPage():
    from Interface.LoginInterface import LoginInterface
    LoginInterface()


def RegisterPage():
    from Interface.RegisterInterface import RegisterInterface
    RegisterInterface()


def AdminPage():
    from Interface.AdminLoginInterface import AdminLoginUI
    AdminLoginUI()


def init():
    CLEAR()
    print("  \n\x1B[1;31m       Welcome To Booking Application  \n")

    operation = int(input("\x1B[2;32m"
                          "1) Login to booking system\n"
                          "2) Create an account\n"
                          "3) Exit\n\n"
                          "0) Admin Login\n->"))
    CLEAR()
    match operation:
        case 1:
            LoginPage()
        case 2:
            RegisterPage()
        case 3:
            exit(1)
        case 0:
            AdminPage()
        case _:
            print("Please Enter A Valid Option")
            exit(1)


def checkCMD():
    print(int(sys.argv[1]))
    try:
        if int(sys.argv[1]) == 99:
            return True
    except IndexError:
        return False


if __name__ == '__main__':
    #if checkCMD():
    init()
