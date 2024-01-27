import os
import time

from Classes.AssistClass import getEmail, getPassword
from Classes.LoginClass import LoginClass
from Interface.ClientInterface import ClientInterface


class LoginInterface:
    def __init__(self):
        self.email = getEmail()
        self.password = getPassword()
        login_process = LoginClass(self.email, self.password)
        if login_process.ClientLogin():
            print("Login successful")
            time.sleep(0.6)
            self.clear_screen()
            ClientInterface(self.email, self.password)
        else:
            print("Client not found.")
            time.sleep(0.5)
            self.clear_screen()
            self.retry_login()

    @staticmethod
    def clear_screen():
        os.system('cls')

    def retry_login(self):
        print("Would you like to try logging in again?")
        operation = input("Enter 'yes' to retry or any other key to exit: ")
        if operation.lower() == 'yes':
            self.clear_screen()
            LoginInterface()
        else:
            print("Exiting...")
            time.sleep(1)
            exit()
