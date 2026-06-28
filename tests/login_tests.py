import allure

from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://ok.ru/"

EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"


#### ------- TESTS ------ ####
@allure.suite("Checking authorization form")
@allure.title("Checking error when authorization form is empty")
def test_empty_login_and_password(browser):
    with allure.step(f"Open login page{BASE_URL}"):
        BasePage(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text("empty login") == EMPTY_LOGIN_ERROR

@allure.suite("Checking authorization form")
@allure.step("Checking error when password in authorization form is empty")
def test_empty_password(browser):
    with allure.step(f"Open the login page{BASE_URL}"):
        BasePage(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.enter_login()
    login_page.click_login()
    assert login_page.get_error_text("empty password") == EMPTY_PASSWORD_ERROR