import unittest

from e2e.login_page.login import SuccessfulLogin


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SuccessfulLogin("valid_username_and_password"))
    suite.addTest(SuccessfulLogin("just_testing_login_command"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
