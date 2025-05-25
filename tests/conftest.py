import curl
import pytest
from selenium import webdriver
from data import Data
from locators.login_locators import LoginPageLocators
from locators.main_locators import MainPageLocators


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(curl.URL)
    elif request.param == "firefox":
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get(curl.URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.execute_script("arguments[0].click();", driver.find_element(*MainPageLocators.MAIN_PAGE_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(Data.TEST_EMAIL)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(Data.TEST_PASSWORD)
    driver.execute_script("arguments[0].click();", driver.find_element(*LoginPageLocators.LOGIN_BUTTON))
    return driver

