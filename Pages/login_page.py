from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'email')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[4]/div/button')
        self.error_message = (By.XPATH, '/html/body/div/div/div/div[1]/div/form/div[1]/div/span/strong')
        #self.success_message = (By.XPATH, '//div[@class="alert alert-success"]')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def clear_username(self):
        self.driver.find_element(*self.username_input).clear()

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def submit(self, password):
        self.driver.find_element(*self.password_input).send_keys(Keys.RETURN)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_success_message_displayed(self):
        return self.driver.find_element(*self.success_message).is_displayed()
    
    def perform_login(self, username, password):
        self.driver.find_element(*self.username_input).clear()        
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.RETURN)
        self.driver.find_element(*self.login_button).click()
        #error_message = self.driver.find_element(*self.error_message).text
        #success_message_displayed = self.driver.find_element(*self.success_message).is_displayed()

        #return error_message