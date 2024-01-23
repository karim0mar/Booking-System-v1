import os
import time

import main
from Classes.AssistClass import getEmail, getPassword
from Classes.LoginClass import LoginClass
from Interface.ClientInterface import ClientInterface


class LoginInterface:
    def __init__(self):
        self.email = getEmail()
        self.password = getPassword()
        LoginProcess = LoginClass(self.email, self.password)
        if LoginProcess.ClientLogin():
            print("Login successful")
            time.sleep(0.6)
            os.system("cls")
            ClientInterface(self.email, self.password)
        else:
            print("Client not found.")
            time.sleep(0.5)
            os.system("cls")
            main.init()
