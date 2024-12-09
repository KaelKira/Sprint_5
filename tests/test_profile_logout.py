from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators


class TestProfileLogout:
    def test_logout_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.EXIT)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.AUTH_BUTTON))
        assert driver.find_element(*Locators.AUTH_BUTTON).text == 'Войти'
