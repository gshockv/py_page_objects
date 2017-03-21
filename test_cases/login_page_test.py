
from pages import login_page_object as lpo

class LoginPageTestCase:
    def __init__(self):
        self.loginPage = lpo.LoginPageObject()

    def testCase1(self):
        print self.loginPage.userNameTextField()

    def testCase2(self):
        print self.loginPage.passwordTextField()
        print self.loginPage.userNameTextField()

