from selenium.webdriver.common.by import By

class Locators:
    EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')
    AUTH_BUTTON = (By.XPATH, './/button[text() = "Войти"]')