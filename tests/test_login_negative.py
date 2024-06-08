import time
import pytest
from selenium.webdriver.common.by import By

from page_object.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")
                              ])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # create instance of the login_page class
        login_page = LoginPage(driver)
        # Open page
        login_page.open()

        login_page.execute_login(username, password)
        # Verify error message is displayed
        assert login_page.get_error_message() == expected_error_message, "Error message is not displayed"

        """
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed, but it should be"
        assert error_message.text == expected_error_message\
            , "Error message is not expected"
            """

    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed, but it should be"
        assert error_message.text == "Your username is invalid!", "Error message is not expected"

    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed(), "Error message is not displayed, but it should be"
        assert error_message.text == "Your password is invalid!", "Error message is not expected"
