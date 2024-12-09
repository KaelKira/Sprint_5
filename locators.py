from selenium.webdriver.common.by import By
from constans import Constants


class Locators:
    EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')
    AUTH_BUTTON = (By.XPATH, './/button[text() = "Войти"]')
    EXIT = (By.XPATH, './/button[text()= "Выход"]')
    PROFILE = (By.XPATH, './/p[text()="Личный Кабинет"]')
    HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')
    ORDER_LIST_HEADER = (By.XPATH, './/h1[text()="Лента заказов"]')
    CONSTRACTOR_TAB = (By.XPATH, './/p[text()="Конструктор"]')
    ENTER_TO_PROFILE_BUTTON = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    ORDER_LIST = (By.XPATH, './/p[text() = "Лента Заказов"]')
    LOGO = (By.XPATH, './/header/nav/div')
    MAKE_AN_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    ENTER_LINK = (By.XPATH, './/a[text()="Войти"]')
    RESER_PASSWORD = (By.XPATH, './/a[text()="Восстановить пароль"]')
    RESER_PASSWORD_BUTTON = (By.XPATH, './/button[text()="Восстановить"]')
    FOR_EMAIL = (By.XPATH, f'.//input[@value = "{Constants.EMAIL}"]')
    REGESTRATION_NAME = (By.XPATH, './/label[text()="Имя"]/parent::div/input')
    REGESTRATION_EMAIL = (By.XPATH, './/label[text()="Email"]/parent::div/input')
    REGESTRATION_PASSWORD = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')
    REGESTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
    REGESTRATION_LINK = (By.XPATH, './/a[text()="Зарегистрироваться"]')
    EXISTED_USER = (By.XPATH, './/p[text()="Такой пользователь уже существует"]')
    WRONG_PASSWORD = (By.XPATH, './/p[text()="Некорректный пароль"]')
    EMAIL_FOR_RESTORE = (By.XPATH, './/input')