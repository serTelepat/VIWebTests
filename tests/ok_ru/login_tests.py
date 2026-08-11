import allure

from core.base_test import browser
from pages.base_page import BasePageHelper
from pages.ok_ru.login_page import LoginPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://ok.ru/"

LOGIN_TEXT = "login_gav_gav"
PASSWORD_TEXT = "123QF"

EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"
INCORRECT_LOGIN_DATA = "Неправильно указан логин и/или пароль"


#### ------- TESTS ------ ####
@allure.suite("Checking authorization form")
@allure.title("Checking error when authorization form is empty")
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_ERROR

@allure.suite("Checking authorization form")
@allure.title("Checking error when password is empty")
def test_empty_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.enter_login(LOGIN_TEXT)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_PASSWORD_ERROR

@allure.suite("Checking authorization form")
@allure.title("Checking error when login and/or password are incorrect")
def test_incorrect_login_datas(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.enter_login(LOGIN_TEXT)
    login_page.enter_password(PASSWORD_TEXT)
    login_page.click_login()
    assert login_page.get_error_text() == INCORRECT_LOGIN_DATA