import time

import pytest
from selenium.webdriver.common.by import By

from page_object.logged_in_successfully import LoggedInSuccessfullyPage
from page_object.login_page import LoginPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # create instance of the login_page class
        login_page = LoginPage(driver)
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.execute_login(username='student', password='Password123')

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, 'Actual url not match'

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_page.header == "Logged In Successfully", 'text doesn\'t match'

        # Verify button Log out is displayed on the new page
        assert logged_in_page.is_logout_button_displayed() , 'logout should be visible'



        """
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
        logout_button = driver.find_element(By.XPATH,
                                            "//a[@href='https://practicetestautomation.com/practice-test-login/']")
        assert logout_button.is_displayed()
        """
