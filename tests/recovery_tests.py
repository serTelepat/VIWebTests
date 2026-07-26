import allure

from core.base_test import browser
from pages.base_page import BasePageHelper
from pages.login_page import LoginPageHelper
from pages.recovery_page import RecoveryPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://sn.rv-school.ru/"

LOGIN_TEXT = "login_gav_gav"
PASSWORD_TEXT = "123"


@allure.suite("Checking the user account recovery")
@allure.title("Checking the redirection to recovery after unsuccessful attempts of login")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.enter_login(LOGIN_TEXT)
    login_page.enter_password(PASSWORD_TEXT)

    login_page.click_login_until_appearing_recover_form()
    login_page.click_recovery()

    RecoveryPageHelper(browser)