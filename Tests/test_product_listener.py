import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from Pages.login_page import LoginPage
from Pages.product_page import productPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print(f"Begin Create product transaction: [{datetime.datetime.now()}]")

    def after_click(self, element, driver):
        print(f"End Create product transaction: [{datetime.datetime.now()}]")

class TestProductCreation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://demo.backpackforlaravel.com/admin/login')
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        self.event_driver = EventFiringWebDriver(self.driver, ProductListener())
        self.event_driver.get('https://demo.backpackforlaravel.com/admin/product/create')
        self.product_page = productPage(self.event_driver)

    def test_product_creation(self):
        self.login_page.perform_login('admin@example.com', 'admin')
        self.product_page.saving_data('test product..', '123456')

        # Example: Logging the end time of the operation
        print("Login and product creation completed.")

    def tearDown(self):
        self.event_driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()