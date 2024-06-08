import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_object.exceptions_page import ExceptionsPage


class TestExceptions:

    #@pytest.mark.exceptions
    def test_no_such_elementException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "row_two_not visible"

        """
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        timeout = 5
        wait = (WebDriverWait(driver, timeout))
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//input[not(@disabled=\"true\")]")))

        assert row_2_input_element.is_displayed(), "row 2 input should be displayed but it's not "
        """

    # @pytest.mark.exceptions
    def test_elementNotInteractableException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food()
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "confirmation text should be displayed"

        """ driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        timeout = 10
        wait = (WebDriverWait(driver, timeout))
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//input[not(@disabled=\"true\")]")))
        assert row_2_input_element.is_displayed(), "row 2 input should be displayed but it's not "

        row_2_input_element.send_keys("pasta")

        save_button = driver.find_element(By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
        save_button.click()

        text_saved_conf = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # text_saved_conf = driver.find_element(By.ID, "confirmation")
        assert text_saved_conf.is_displayed()
        assert text_saved_conf.text == "Row 2 was saved", "confirmation text should be displayed"
        """

    # @pytest.mark.exceptions
    def test_InvalidElementStateException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.modify_row_1_input("Sushi")
        assert exception_page.get_confirmation_message() == "Row 1 was saved", "confirmation text should be displayed"

        """
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        edit_button = driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='edit_btn']")
        edit_button.click()

        row_one_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        timeout = 5
        wait = (WebDriverWait(driver, timeout))
        wait.until(ec.element_to_be_clickable(row_one_locator))
        row_one_locator.clear()

        row_one_locator.send_keys("sushi")
        save_button = driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
        assert save_button.is_displayed()
        save_button.click()

        text_saved_conf = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        # text_saved_conf = driver.find_element(By.ID, "confirmation")
        assert text_saved_conf.is_displayed()
        assert text_saved_conf.text == "Row 1 was saved", "confirmation text should be displayed"
        """

    # @pytest.mark.exceptions
    def test_stale_reference_element_exceptions(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert not exception_page.are_instructions_displayed(), "instruction text element should not be displayed"

        """driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # instruction_text = driver.find_element(By.ID, "instructions")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        # assert not instruction_text.is_displayed(), "instruction text element should not be displayed"
        timeout = 10
        wait = WebDriverWait(driver, timeout)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "instruction text element should not be displayed")"""

    @pytest.mark.exceptions
    def test_time_out_exceptions(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"


        """driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        wait = WebDriverWait(driver, 8)
        assert wait.until(
            ec.visibility_of_element_located((By.XPATH, "//div[@id='row2']/input")),
            "row 2 input should be displayed but it's not ")"""
