import json
import os
import time


class RegisterInterface():

    def __init__(self):
        print("         Welcome to the register page ..         \n")
        firsName = input("Enter your first name: \n")
        lastName = input("Enter your last name: \n")
        phoneNumber = input("Enter your phone number: \n")
        email = input("Enter your email address: \n")
        password = input("Enter your password: \n")

