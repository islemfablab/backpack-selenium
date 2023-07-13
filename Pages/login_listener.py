from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import datetime
from login_page import LoginPage

class LoggingListener(AbstractEventListener):
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def before_navigate_to(self, url, driver):
        print(f"Begin transaction: [{datetime.datetime.now()}]")

    def after_click(self, element, driver):
        print(f"End transacction : [{datetime.datetime.now()}]")

    # Implement other event methods as needed

# Set up the WebDriver and wrap it with EventFiringWebDriver
log_file_path = 'C:/Users/fabla/PycharmProjects/pythonProject/Report/note.txt'
driver = webdriver.Chrome()
event_driver = EventFiringWebDriver(driver, LoggingListener(log_file_path))

# Navigate to the login page
event_driver.get('https://demo.backpackforlaravel.com/admin/login')

# Create an instance of the LoginPage
login_page = LoginPage(event_driver)

# Perform the login operation
login_page.perform_login('admin@example.com', 'admin')

# Example: Logging the end time of the operation
print(".........Login completed.")

# Quit the WebDriver
event_driver.quit()
