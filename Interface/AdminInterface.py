from Classes.AdminData import checkAdminEmailExisted


def AdminPageUI(email, password):
    if not checkAdminEmailExisted(email,password):
        exit(1)
    else:
        print("         Welcome to the admin control page ..         \n")

    pass
