from random import randint
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def new_login():
    login = 'amatveev_' + str(randint(100,999)) + '@yandex.ru'
    return login