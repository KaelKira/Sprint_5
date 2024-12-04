from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators


class TestProfile:
    #Переход по клику на «Личный кабинет»
    def test_profile_form_lk_link_page_success(self, driver):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/p[text()="Личный Кабинет"]'))).click()
        xpathforemail = f'.//input[@value = "{Constants.EMAIL}"]'

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, xpathforemail)))

        assert driver.find_element(By.XPATH, xpathforemail).get_dom_attribute('value') == Constants.EMAIL

        driver.quit()