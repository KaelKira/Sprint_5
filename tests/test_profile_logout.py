from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators

class TestProfileLogout:
#Переход по клику на «Личный кабинет»
    def test_logout_success(self, driver):
        driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/p[text()="Личный Кабинет"]'))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/button[text()= "Выход"]'))).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/button[text()= "Войти"]'))).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()