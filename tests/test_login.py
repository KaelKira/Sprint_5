from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
from constans import Constants
from locators import Locators


class TestLogin:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_form_main_page_success(self, driver):
        driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]').click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Оформить заказ"]')))

        assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').text == 'Оформить заказ'

        driver.quit()


    #вход через кнопку «Личный кабинет»
    def test_login_form_header_lk_button_success(self, driver):
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Оформить заказ"]')))

        assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').text == 'Оформить заказ'

        driver.quit()

    #вход через кнопку в форме регистрации - см тест test_registration_valid_data_success

    #вход через кнопку в форме восстановления пароля страница forgot-password
    def test_login_reset_password_link_first_page_success(self, driver):
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(By.XPATH, './/a[text()="Восстановить пароль"]').click()

        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/a[text()="Войти"]')))
        driver.find_element(By.XPATH, './/a[text()="Войти"]').click()

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, './/button[text() = "Войти"]'))
        )

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Оформить заказ"]')))

        assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').text == 'Оформить заказ'

        driver.quit()

    #вход через кнопку в форме восстановления пароля страница reset-password
    def test_login_reset_password_link_second_page_success(self, driver):
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()

        #нажимаем восстановить пароль
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/a[text()="Восстановить пароль"]')))
        driver.find_element(By.XPATH, './/a[text()="Восстановить пароль"]').click()

        # вводим email для восстановления
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Восстановить"]')))
        driver.find_element(By.XPATH, './/input').send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, './/button[text()="Восстановить"]').click()

        #нажимаем войти
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, './/a[text()="Войти"]')))
        time.sleep(2)
        driver.find_element(By.XPATH, './/a[text()="Войти"]').click()

        #логинимся
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, './/button[text() = "Войти"]'))
        )
        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Оформить заказ"]')))

        assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').text == 'Оформить заказ'

        driver.quit()