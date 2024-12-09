from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from helpers import new_login


class TestRegistration:
    def test_registration_valid_data_success(self, driver):
        login = new_login()
        # открываем страницу с регистрацией
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGESTRATION_LINK))
        driver.find_element(*Locators.REGESTRATION_LINK).click()

        #регистрируемся
        driver.find_element(*Locators.REGESTRATION_NAME).send_keys('Kai')
        driver.find_element(*Locators.REGESTRATION_EMAIL).send_keys(login)
        driver.find_element(*Locators.REGESTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(login)
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER))

        assert driver.find_element(*Locators.MAKE_AN_ORDER).text == 'Оформить заказ'


    def test_registration_double_registration_error(self, driver):
        login = new_login()
        # открываем страницу с регистрацией
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGESTRATION_LINK))
        driver.find_element(*Locators.REGESTRATION_LINK).click()

        #регистрируемся
        driver.find_element(*Locators.REGESTRATION_NAME).send_keys('Kai')
        driver.find_element(*Locators.REGESTRATION_EMAIL).send_keys(login)
        driver.find_element(*Locators.REGESTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()


        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGESTRATION_LINK))
        driver.find_element(*Locators.REGESTRATION_LINK).click()

        # повторная регистрация с существующими кредами
        driver.find_element(*Locators.REGESTRATION_NAME).send_keys('Kai')
        driver.find_element(*Locators.REGESTRATION_EMAIL).send_keys(login)
        driver.find_element(*Locators.REGESTRATION_PASSWORD).send_keys('123456')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.EXISTED_USER))
        assert driver.find_element(*Locators.EXISTED_USER).text == 'Такой пользователь уже существует'


    def test_registration_password_less_then_6_simbl_error(self, driver):
        login = new_login()
        # открываем страницу с регистрацией
        driver.find_element(*Locators.PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.REGESTRATION_LINK))
        driver.find_element(*Locators.REGESTRATION_LINK).click()

        #регистрируемся
        driver.find_element(*Locators.REGESTRATION_NAME).send_keys('Kai')
        driver.find_element(*Locators.REGESTRATION_EMAIL).send_keys(login)
        driver.find_element(*Locators.REGESTRATION_PASSWORD).send_keys('12345')
        driver.find_element(*Locators.REGESTRATION_BUTTON).click()

        assert driver.find_element(*Locators.WRONG_PASSWORD).text == 'Некорректный пароль'


