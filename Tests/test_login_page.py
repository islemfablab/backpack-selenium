from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.login_page import LoginPage
import time


# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other browser driver as per your preference
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get('https://demo.backpackforlaravel.com/admin/login')

# Create an instance of the LoginPage
login_page = LoginPage(driver)

# Begin bloc test
print('Begin login tests with credentiel ...')

print('.....Login with incorrect credentials')
# Wait for the error message to be displayed
error_message  = login_page.perform_login("test", "test")
print(f"messsage new function : {error_message} ")
time.sleep(5)
print('.....End Test.')

print('.....Login with correct credentials')
# Wait for the error message to be displayed
error_message  = login_page.perform_login("admin@example.com", "admin")
print(f"messsage new function : {error_message} ")
time.sleep(5)
print('.....End Test.')