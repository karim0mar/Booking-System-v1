import os
import time

from Classes.AssistClass import readData
from Classes.ClientData import showClients, removeClientWithEmail, checkEmailExisted, ClientsNumber


def AdminClientRemover(email, password):
    if ClientsNumber() > 0:
        print("         Welcome to Client Remover       ")
        showClients()
        print("\x1b[48;2;255;0;0m Enter 0 to back")
        operation = input("\033[0m\x1B[3;33m"
                          " rem (Client Email) to remove a client \n"
                          "\x1B[3;31m Note! rem * removes all client \n"
                          " \n->")
        os.system("cls")
        match operation:
            case "0":
                from Interface.AdminInterface import clientPanel
                clientPanel(email, password)
            case _:
                if "rem" in operation:
                    clientEmail = operation.split("rem ")[1]
                    if clientEmail == '*':
                        clientsData = readData("Clients")["clients"]
                        for client in clientsData:
                            removeClientWithEmail(client["email"])

                    else:
                        if checkEmailExisted(clientEmail):
                            if removeClientWithEmail(clientEmail):
                                print("Client " + clientEmail + " removed")
                            else:
                                print("failed to remove")
                        else:
                            print("Client " + clientEmail + " does not exist")
                    time.sleep(2)
                    os.system("cls")
                    AdminClientRemover(email, password)
    else:
        print("No clients in the system")
        time.sleep(2)
        os.system("cls")
        from Interface.AdminInterface import clientPanel
        clientPanel(email, password)
