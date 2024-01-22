import json
import os
import time

import main
from Classes.ClientData import ClientData, checkEmailExisted
from Classes.LoginClass import LoginClass
from Classes.RegisterClass import RegisterClass, registerEmail
from Interface.ClientInterface import ClientInterface


class RegisterInterface:

    def __init__(self):
        print("         Welcome to the register page ..         \n")
        firsName = input("Enter your first name: \n")
        lastName = input("Enter your last name: \n")
        phoneNumber = input("Enter your phone number: \n")
        email = input("Enter your email address: \n")
        password = input("Enter your password: \n")
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
