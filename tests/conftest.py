import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(Urls.MAIN_URL)
    yield browser
    browser.quit()