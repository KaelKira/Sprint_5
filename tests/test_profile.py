from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators


class TestProfile:
    #Переход по клику на «Личный кабинет»
    def test_profile_form_lk_link_page_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.FOR_EMAIL))

        assert driver.find_element(*Locators.FOR_EMAIL).get_dom_attribute('value') == Constants.EMAIL
