from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestRegistration:
    def test_registration_valid_data_success(self, new_login, driver):
        # открываем страницу с регистрацией
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
            By.XPATH, './/a[text()="Зарегистрироваться"]')))
        driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()

        #регистрируемся
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Kai')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys(new_login)
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('123456')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text() = "Войти"]')))

        driver.find_element(*Locators.EMAIL).send_keys(new_login)
        driver.find_element(*Locators.PASSWORD).send_keys('123456')
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            (By.XPATH, './/button[text()="Оформить заказ"]')))

        assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').text == 'Оформить заказ'

        driver.quit()

    def test_registration_double_registration_error(self, driver, new_login):
        # открываем страницу с регистрацией
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
            By.XPATH, './/a[text()="Зарегистрироваться"]')))
        driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()

        #регистрируемся
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Kai')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys(new_login)
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('123456')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()


        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
            By.XPATH, './/a[text()="Зарегистрироваться"]')))
        driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()

        # повторная регистрация с существующими кредами
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Kai')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys(new_login)
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('123456')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
            By.XPATH, './/p[text()="Такой пользователь уже существует"]')))
        assert driver.find_element(By.XPATH, './/p[text()="Такой пользователь уже существует"]').text == 'Такой пользователь уже существует'

        driver.quit()

    def test_registration_password_less_then_6_simbl_error(self, driver, new_login):
        # открываем страницу с регистрацией
        driver.find_element(By.XPATH, './/p[text() = "Личный Кабинет"]').click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((
            By.XPATH, './/a[text()="Зарегистрироваться"]')))
        driver.find_element(By.XPATH, './/a[text()="Зарегистрироваться"]').click()

        #регистрируемся
        driver.find_element(By.XPATH, './/label[text()="Имя"]/parent::div/input').send_keys('Kai')
        driver.find_element(By.XPATH, './/label[text()="Email"]/parent::div/input').send_keys(new_login)
        driver.find_element(By.XPATH, './/label[text()="Пароль"]/parent::div/input').send_keys('12345')
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()

        assert driver.find_element(By.XPATH, './/p[text()="Некорректный пароль"]').text == 'Некорректный пароль'

        driver.quit()


