from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Pages.Login import Login

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('https://demo.backpackforlaravel.com/admin/login')

login = Login(driver)
login.start_login("test", "test")

