from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class productPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.XPATH, '/html/body/div[1]/main/div/div/div/form/div[1]/div/div/div[1]/div/div[1]/input')
        self.basic_info = (By.XPATH, '/html/body/div[1]/main/div/div/div/form/div[1]/div/ul/li[2]/a')
        self.price_input = (By.NAME, 'price')
        self.save_button = (By.XPATH, '//*[@id="saveActions"]/div/button[1]/span[2]')
        self.error_message = (By.XPATH, '/html/body/div[1]/main/div/div/div/div/ul/li')
        self.success_message = (By.XPATH, '//div[@class="alert alert-success"]')

    def enter_name(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def clear_name(self):
        self.driver.find_element(*self.name_input).clear()

    def enter_price(self, price):
        self.driver.find_element(*self.price_input).send_keys(price)

    def submit(self, price):
        self.driver.find_element(*self.price_input).send_keys(Keys.RETURN)

    def click_save(self):
        self.driver.find_element(*self.save_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_success_message_displayed(self):
        current_url = self.driver.current_url
        expected_url = "https://demo.backpackforlaravel.com/admin/product"
        return self.assertEqual(current_url, expected_url, "Current URL should be equal to the expected URL")

    def saving_data(self, name, price):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.basic_info).click()
        self.driver.find_element(*self.price_input).send_keys(price)
        self.driver.find_element(*self.save_button).click()