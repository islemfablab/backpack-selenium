from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from Pages.product_page import productPage
from utility import generate_random_string
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other browser driver as per your preference
wait = WebDriverWait(driver, 10)
driver.get('https://demo.backpackforlaravel.com/admin/login')
# Retrieve the CSRF token value from the login form

login = driver.find_element(By.ID,"email")
login.clear()
login.send_keys("admin@example.com")
pwd = driver.find_element(By.ID,"password")
pwd.send_keys("admin")
pwd.send_keys(Keys.RETURN)  # Press Enter key
remember = driver.find_element(By.NAME,"remember")
remember.click()
btn_submit=driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/form/div[4]/div/button")
btn_submit.click()
time.sleep(3)
# Navigate to the save page
driver.get('https://demo.backpackforlaravel.com/admin/product/create')
time.sleep(3)
# Create an instance of the savePage
product_page = productPage(driver)


# Test with incorrect credentials
print('................Begin test with empty data ..................')

# product_page.enter_name('')
# product_page.enter_price('')
product_page.click_save()

try:
    # Wait for the error message to be displayed
    wait.until(EC.visibility_of_element_located(product_page.error_message))
    error_message = product_page.get_error_message()
    print(f"Error message: {error_message}")
    print('Verification with empty data done successfuly...')
    time.sleep(5)

except TimeoutException:
    print('save with incorrect credentials failed!')
    time.sleep(5)

print('................Begin test with large data ..................')

random_string = generate_random_string(300)
product_page.enter_name(random_string)
product_page.click_save()

try:
    # Wait for the error message to be displayed
    wait.until(EC.visibility_of_element_located(product_page.error_message))
    error_message = product_page.get_error_message()
    expected_message = "The name may not be greater than 255 characters."
    #product_page.assertEqual(error_message, expected_message, f"Expected error message: '{expected_message}', but got: '{error_message}'")
    print(f"Error message: {error_message}")
    print('Verification with large data done successfuly...')
    time.sleep(5)

except TimeoutException:
    print('save with incorrect credentials failed!')
    time.sleep(5)


# try:
#     # Wait for the success message to be displayed
#     #wait.until(EC.visibility_of_element_located(product_page.success_message))
#     # Test with correct credentials
#     product_page.clear_name()
#     product_page.enter_name('admin@example.com')
#     product_page.enter_price('admin')
#     product_page.click_save()
#     remember = driver.find_element(By.NAME,"remember")
#     remember.click()
#     product_page.submit('admin')
#     #wait.until(lambda driver: "dashboard" in driver.current_url or driver.current_url == "https://demo.backpackforlaravel.com/admin/dashboard")
#     wait.until(lambda driver: "dashboard" in driver.current_url or driver.current_url == "https://demo.backpackforlaravel.com/admin/dashboard")
#     print('save with correct credentials passed!')
#     time.sleep(5)
# except TimeoutException:
#     print('save with correct credentials failed!')
#     time.sleep(5)
# Close the browser
# driver.quit()
