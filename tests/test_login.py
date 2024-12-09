from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_form_main_page_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER))

        assert driver.find_element(*Locators.MAKE_AN_ORDER).text == 'Оформить заказ'



    #вход через кнопку «Личный кабинет»
    def test_login_form_header_lk_button_success(self, driver):
        driver.find_element(*Locators.PROFILE).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER))

        assert driver.find_element(*Locators.MAKE_AN_ORDER).text == 'Оформить заказ'


    #вход через кнопку в форме регистрации - см тест test_registration_valid_data_success

    #вход через кнопку в форме восстановления пароля страница forgot-password
    def test_login_reset_password_link_first_page_success(self, driver):
        driver.find_element(*Locators.PROFILE).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.RESER_PASSWORD).click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            Locators.ENTER_LINK))

        driver.find_element(*Locators.ENTER_LINK).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.AUTH_BUTTON)
        )

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER))

        assert driver.find_element(*Locators.MAKE_AN_ORDER).text == 'Оформить заказ'


    #вход через кнопку в форме восстановления пароля страница reset-password
    def test_login_reset_password_link_second_page_success(self, driver):
        driver.find_element(*Locators.PROFILE).click()

        #нажимаем восстановить пароль
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.RESER_PASSWORD))
        driver.find_element(*Locators.RESER_PASSWORD).click()

        # вводим email для восстановления
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.RESER_PASSWORD_BUTTON))
        driver.find_element(*Locators.EMAIL_FOR_RESTORE).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.RESER_PASSWORD_BUTTON).click()

        #ну как есть
        WebDriverWait(driver, 10).until(
            expected_conditions.staleness_of(driver.find_element(*Locators.ENTER_LINK)))

        new_element = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(Locators.ENTER_LINK)  # Найти новый элемент
        )
        new_element.click()

        #логинимся
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(Locators.AUTH_BUTTON)
        )
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.MAKE_AN_ORDER))

        assert driver.find_element(*Locators.MAKE_AN_ORDER).text == 'Оформить заказ'
