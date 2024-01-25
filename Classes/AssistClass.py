import json
import re

from Classes.ClientData import checkEmailExisted


def readData(fileName):
    file_path = f"Data/{fileName}.json"
    file = open(file_path)
    data = json.load(file)
    file.close()
    return data


def writeData(fileName, data):
    writeFile = open(f"Data/{fileName}.json", "w")
    release = json.dumps(data, indent=4, separators=(',', ': '))
    writeFile.write(release)
    writeFile.close()


def getFName():
    fName = input("Enter your first name: \n->")
    if len(fName) > 10 or len(fName) <= 1:
        print("Please enter a valid name")
        getFName()
    else:
        return fName


def getLName():
    lName = input("Enter your last name: \n->")
    if len(lName) > 10 or len(lName) <= 1:
        print("Please enter a valid name")
        getLName()
    else:
        return lName


def checkEmailSyntax(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def getEmail():
    email = input("Enter your email address: \n->")
    if checkEmailSyntax(email):
        return email
    else:
        print("Please enter a valid email")
        return getEmail()


def getEmailAndCheck():
    email = input("Enter your email address: \n->")
    if checkEmailSyntax(email):
        if not checkEmailExisted(email):
            return email
        else:
            print("Email already exists. Please try again")
            return getEmail()
    else:
        print("Please enter a valid email")
        return getEmail()


def getPassword():
    password = input("Enter your password: \n->")
    if len(password) > 15 or len(password) < 1:
        print("Please enter a valid password")
        return getPassword()
    else:
        return password


def getPhoneNumber():
    phoneNumber = input("Enter your phone number: \n->")
    if 12 < len(phoneNumber) < 8:
        print("Please enter a valid phone number")
        return getPhoneNumber()
    else:
        return phoneNumber


def getBankNumber():
    BankNumber = input("\033[0;35mEnter your bank account number: \n ->")
    if 12 >= len(BankNumber) >= 8:
        return BankNumber
    else:
        print("Please enter a valid bank account number")
        return getBankNumber()