# Login Page object definition

class LoginPageObject:
    def __init__(self):
        self.userNameLocator = "UserName Locator"
        self.passwordLocator = "Password Locator"

    def userNameTextField(self):
        self.userNameLocator += " Was Found"
        return self.userNameLocator

    def passwordTextField(self):
        self.passwordLocator += " Was Found"
        return self.passwordLocator
