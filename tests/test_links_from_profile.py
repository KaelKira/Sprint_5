from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constans import Constants
from locators import Locators



#переход по клику на «Конструктор»
class TestLinks:
    def test_link_constructor_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.EXIT))

        driver.find_element(*Locators.CONSTRACTOR_TAB).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.HEADER))

        assert driver.find_element(*Locators.HEADER).text == 'Соберите бургер'

        driver.quit()

    #переход по клику на логотип Stellar Burgers
    def test_link_logo_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.EXIT))

        driver.find_element(*Locators.LOGO).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.HEADER)).click()

        assert driver.find_element(*Locators.HEADER).text == 'Соберите бургер'

        driver.quit()

    # переход по клику Лента Заказов
    def test_link_orders_list_success(self, driver):
        driver.find_element(*Locators.ENTER_TO_PROFILE_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.AUTH_BUTTON))

        driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(
            Locators.PROFILE)).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            Locators.EXIT))

        driver.find_element(*Locators.ORDER_LIST).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locators.ORDER_LIST_HEADER)).click()

        assert driver.find_element(*Locators.ORDER_LIST_HEADER).text == 'Лента заказов'

        driver.quit()
