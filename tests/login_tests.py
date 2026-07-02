import allure

from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://sn.rv-school.ru/"

LOGIN_TEXT = "login_gav_gav"

EMPTY_LOGIN_OR_PASSWORD_ERROR = "Введите телефон, email или логин и пароль."
INCORRECT_LOGIN_DATA = ("Пользователь с таким телефоном, почтой или логином не найден. "
                        + "Проверьте данные и попробуйте снова.")


#### ------- TESTS ------ ####
@allure.suite("Checking authorization form")
@allure.title("Checking error when authorization form is empty")
def test_empty_login_and_password(browser):
    with allure.step(f"Open login page{BASE_URL}"):
        BasePage(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_OR_PASSWORD_ERROR

@allure.suite("Checking authorization form")
@allure.title("Checking error when password in authorization form is empty")
def test_empty_password(browser):
    with allure.step(f"Open the login page{BASE_URL}"):
        BasePage(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.enter_login(LOGIN_TEXT)
    login_page.click_login()
    assert login_page.get_error_text() == EMPTY_LOGIN_OR_PASSWORD_ERROR