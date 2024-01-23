import os
import time
import main
from Classes.AssistClass import *
from Classes.ClientData import checkEmailExisted
from Classes.RegisterClass import registerEmail
from Interface.ClientInterface import ClientInterface


class RegisterInterface:

    def __init__(self):
        print("         Welcome to the register page ..         \n")
        firsName = getFName()
        lastName = getLName()
        phoneNumber = getPhoneNumber()
        email = getEmailAndCheck()
        password = getPassword()
        fullName = firsName + " " + lastName
        if not checkEmailExisted(email):
            if registerEmail(email, password, fullName, phoneNumber):
                print("Email registered successfully..")
                time.sleep(1)
                os.system("cls")
                ClientInterface(email, password)
        else:
            print("Email already registered.")
            time.sleep(0.5)
            main.init()
