from Classes.AdminData import AdminData
from Classes.ClientData import ClientData


class LoginClass:
    ID = None

    def __init__(self, _email, _password):
        self.email = _email
        self.password = _password

    def ClientLogin(self):
        LoginData = ClientData(self.email, self.password)
        return LoginData.LoginStatues

    def AdminLogin(self):
        LoginData = AdminData(self.email, self.password)
        return LoginData.LoginStatues
