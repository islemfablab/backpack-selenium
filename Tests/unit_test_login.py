import time

from Pages.login_page import LoginPage
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class UnitTestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://demo.backpackforlaravel.com/admin/login')
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_login_with_incorrect_credentials(self):
    #     self.login_page.perform_login("test", "test")
    #     error_message = self.login_page.get_error_message()
    #     self.assertIsNotNone(error_message, "These credentials do not match our records.")
    #     time.sleep(2)
    #
    # def test_empty_login(self):
    #     self.login_page.perform_login("", "test")
    #     error_message = self.login_page.get_error_message()
    #     self.assertIsNotNone(error_message, "These credentials do not match our records.")
    #     time.sleep(5)

    def test_login_with_correct_credentials(self):
        self.login_page.perform_login("admin@example.com", "admin")
        current_url = self.driver.current_url
        expected_url = "https://demo.backpackforlaravel.com/admin/dashboard"
        self.assertEqual(current_url, expected_url, "Current URL should be equal to the expected URL")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=os.path.join(os.getcwd(), 'Report')))
