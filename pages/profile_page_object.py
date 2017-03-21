# describes Profile Page with page object

class ProfilePageObject:
    def __init__(self):
        self.firstNameLocator = "FirstName Locator"
        self.lastNameLocator = "LastName Locator"
        self.avatarLocator = "Avatar Locator"

    def firstNameField(self):
        self.firstNameLocator += " was found"
        return self.firstNameLocator

    def lastNameField(self):
        self.lastNameLocator += " was found"
        return self.lastNameLocator

    def avatarField(self):
        self.avatarLocator += " was found"
        return self.avatarLocator

