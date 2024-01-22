import os
import time

import main
from Classes.LoginClass import LoginClass
from Interface.ClientInterface import ClientInterface


class LoginInterface:
    def __init__(self):
        self.email = input("Enter your email address:\n->")
        self.password = input("Enter your password:\n->")
        LoginProcess = LoginClass(self.email, self.password)
        if LoginProcess.login():
            print("Login successful")
            time.sleep(0.6)
            os.system("cls")
            ClientInterface(self.email, self.password)
        else:
            print("Client not found.")
            time.sleep(0.5)
            os.system("cls")
            main.init()
