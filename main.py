import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.XPATH, "//h1[@class='post-title']")
assert text_locator.text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
logout_button = driver.find_element(By.XPATH, "//a[@href='https://practicetestautomation.com/practice-test-login/']")
assert logout_button.is_displayed()
