from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper


BASE_URL = "https://ok.ru/"
EMPTY_LOGIN_ERROR = "Введите логин"
EMPTY_PASSWORD_ERROR = "Введите пароль"


def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_login()
    assert login_page.get_error_text("empty login") == EMPTY_LOGIN_ERROR

def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.enter_login()
    login_page.click_login()
    assert login_page.get_error_text("empty password") == EMPTY_PASSWORD_ERROR