import unittest
from selenium import webdriver
from support.commands import loginWith, login
from config.credentials import VALID_PASSWORD, VALID_USERNAME


class SuccessfulLogin (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # LP-001
    def valid_username_and_password(self):
        loginWith(self.browser, VALID_USERNAME, VALID_PASSWORD)

    def just_testing_login_command(self):
        login(self.browser)


if __name__ == "__main__":
    unittest.main()
