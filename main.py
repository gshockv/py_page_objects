
# Main starter app

from test_cases import login_page_test as lpt
from pages import profile_page_object as ppo

class Main:
    def startTestsWithCases(self):
        loginPageTest = lpt.LoginPageTestCase()

        print "Starting 1st test case . . ."
        print loginPageTest.testCase1()

        print "\n"

        print "Starting 2nd test case . . ."
        print loginPageTest.testCase2()

    def testProfileWithoutCases(self):

        profilePage = ppo.ProfilePageObject()

        print profilePage.avatarField()
        print profilePage.lastNameField()
        print profilePage.firstNameField()


if __name__ == "__main__":
    starter = Main()
    starter.startTestsWithCases()
    print "\n---------------------------\n"
    starter.testProfileWithoutCases()

