import os
import sys
import time

from Interface.LoginInterface import LoginInterface
from Interface.RegisterInterface import RegisterInterface
from Interface.AdminLoginInterface import AdminLoginUI
from Interface.ClientInterface import ClientInterface


def clear_screen():
    os.system('cls')


def login_page():
    LoginInterface()


def register_page():
    register_data = RegisterInterface()
    register_data.register()
    if register_data.registerStatues:
        ClientInterface(register_data.email, register_data.password)


def admin_page():
    AdminLoginUI()


def initialize():
    clear_screen()
    print("\n\x1B[1;31m       Welcome To Booking Application  \n")
    while True:
        try:
            operation = int(input("\x1B[2;32m"
                                  "1) Login to booking system\n"
                                  "2) Create an account\n"
                                  "3) Exit\n\n"
                                  "0) Admin Login\n->"))
            clear_screen()
            if operation == 1:
                login_page()
            elif operation == 2:
                register_page()
            elif operation == 3:
                sys.exit(1)
            elif operation == 0:
                admin_page()
            else:
                print("Please Enter A Valid Option")
                time.sleep(1.5)
        except ValueError:
            print("Invalid input. Please enter a number.")


def check_command_line_arguments():
    try:
        return int(sys.argv[1]) == 99
    except (IndexError, ValueError):
        return False


if __name__ == '__main__':
    if check_command_line_arguments():
        initialize()
