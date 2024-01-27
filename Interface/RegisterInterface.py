import os
import time
from Classes.AssistClass import *
from Classes.ClientData import checkEmailExisted
from Classes.RegisterClass import registerEmail


class RegisterInterface:

    def __init__(self):
        self.email = None
        self.password = None
        self.registerStatues = False

    def register(self):
        print("         Welcome to the register page ..         \n")
        firsName = getFName()
        lastName = getLName()
        phoneNumber = getPhoneNumber()
        email = getEmailAndCheck()
        password = getPassword()
        fullName = firsName + " " + lastName
        if not checkEmailExisted(email):
            if registerEmail(email, password, fullName, phoneNumber):
                print("\nRegistered successfully..")
                time.sleep(1)
                os.system("cls")
                self.registerStatues = True
                self.email = email
                self.password = password
        else:
            print("\nEmail already registered.")
            time.sleep(0.5)
            import main
            main.initialize()
