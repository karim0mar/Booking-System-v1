import os
import time

from Classes.AssistClass import getEmail, getPassword
from Classes.LoginClass import LoginClass
from Interface.AdminInterface import adminPageUI


def AdminLoginUI():
    print("         Welcome to the admin login page ..         \n")
    email = getEmail()
    password = getPassword()
    LoginProcess = LoginClass(email, password)
    if LoginProcess.AdminLogin():
        print("Login successful")
        time.sleep(0.6)
        os.system("cls")
        adminPageUI(email, password)
    else:
        print("Admin not found.")
        time.sleep(0.5)
        os.system("cls")
        import main
        main.initialize()
    pass
