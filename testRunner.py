import unittest
from e2e.login_page.login import SuccessfulLogin
import chromedriver_autoinstaller
import os

# Check if running on Github Actions
is_running_on_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'

# If running on Github Actions, start virtual display
if is_running_on_github_actions:
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1200, 1200))
    display.start()


chromedriver_autoinstaller.install()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SuccessfulLogin("valid_username_and_password"))
    suite.addTest(SuccessfulLogin("just_testing_login_command"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
