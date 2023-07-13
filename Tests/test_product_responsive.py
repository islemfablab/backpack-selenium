import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ProductResponsivenessTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome()

        self.driver.get('https://demo.backpackforlaravel.com/admin/login')  
        self.driver.find_element(By.ID, 'email').clear()        
        self.driver.find_element(By.ID, 'email').send_keys("admin@example.com")
        self.driver.find_element(By.ID, 'password').send_keys("admin")
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[4]/div/button').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[4]/div/button').click()
    
    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_iPhone_screen(self):

        # Set browser window size for mobile screen
        self.driver.set_window_size(375, 667)  # Example: iPhone 6/7/8 dimensions
        # Navigate to the 'Product' module
        self.driver.get('https://demo.backpackforlaravel.com/admin/product')  # Example: URL for the 'Product' module

        # Verify the visibility and placement of UI elements on mobile screen
        product_list = self.driver.find_element(By.XPATH, '/html/body/div[1]/main/nav/ol')
        time.sleep(2)
        self.assertFalse(product_list.is_displayed(), "Product list element is not visible on iPhone screen")


    def test_tablet_screen(self):
        # Set browser window size for tablet screen
        self.driver.set_window_size(768, 1024)  # Example: iPad dimensions

        # Navigate to the 'Product' module
        self.driver.get('https://demo.backpackforlaravel.com/admin/product')  # Example: URL for the 'Product' module

        # Verify the visibility and placement of UI elements on tablet screen
        product_list = self.driver.find_element(By.XPATH, '//*[@id="bottom_buttons"]/a[1]')
        time.sleep(2)
        self.assertTrue(product_list.is_displayed(), "Product list element is not visible on Tablet screen")



    def test_laptop_screen(self):
        # Set browser window size for tablet screen
        
        self.driver.maximize_window()  # Example: laptop dimensions

        # Navigate to the 'Product' module
        self.driver.get('https://demo.backpackforlaravel.com/admin/product')  # Example: URL for the 'Product' module

        # Verify the visibility and placement of UI elements on tablet screen
        product_list = self.driver.find_element(By.XPATH, '//*[@id="bottom_buttons"]/a[1]')
        time.sleep(2)
        self.assertTrue(product_list.is_displayed(), "Product list element is not visible on Laptop screen")


if __name__ == '__main__':
    unittest.main()
