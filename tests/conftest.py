import curl
import pytest
from selenium import webdriver
from data import Data
from pages.login_page import LoginPage
from pages.main_page import MainPage


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
    main_page = MainPage(driver)
    main_page.click_main_button()
    login_page = LoginPage(driver)
    login_page.print_user_email(Data.TEST_EMAIL)
    login_page.print_user_password(Data.TEST_PASSWORD)
    login_page.click_login_button()
    return driver
