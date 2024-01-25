import os
import time

from Classes.AssistClass import getBankNumber
from Classes.FilmsControl import CURRENCY
from Classes.PayClass import PayClass


def load():
    fetch = "█"

    for i in range(0, 6):
        printString = f'\x1b[38;5;{i}m{fetch}\x1b[0m'
        time.sleep(0.8)
        print("  " + printString, end='')


def PayInterfaceInit(email, password, filmsList):
    payOperation = PayClass(email, password, filmsList)
    os.system("cls")
    print(f"Welcome to Pay Page, your total price is {str(payOperation.getTotalPayment()) + ' ' + CURRENCY}\n\n")
    bankAccount = getBankNumber()
    print("\n\n\nprogressing the payment. please wait...\n")
    load()
    time.sleep(4)
    if payOperation.confirmPayment():
        print("\n\n\t\t Payment Successful. ")
        time.sleep(1.5)
        os.system("cls")
        from Interface.ClientInterface import ClientInterface
        ClientInterface(email, password)
    else:
        print("\n\n\t\t Payment Failed. ")
        time.sleep(3)
