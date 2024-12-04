from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators


#переход по клику на «Конструктор»
class TestLinks:
    def test_link_constructor_success(self, driver):
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

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/button[text()= "Выход"]')))

        driver.find_element(By.XPATH, './/p[text()="Конструктор"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]'))).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    #переход по клику на логотип Stellar Burgers
    def test_link_logo_success(self, driver):
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

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/button[text()= "Выход"]')))

        driver.find_element(By.XPATH, './/header/nav/div').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/h1[text()="Соберите бургер"]'))).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()