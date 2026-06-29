import allure

from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper
from pages.recovery_page import RecoveryPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://ok.ru/"

LOGIN_TEXT = "login_gav_gav"
PASSWORD_TEXT = "123"


@allure.suite("Checking the user account recovery")
@allure.title("Checking the redirection to recovery after unsuccessful attempts of login")
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.enter_login(LOGIN_TEXT)
    login_page.enter_password(PASSWORD_TEXT)

    with allure.step("Attempting login"):
        for attempt in range(3):
            login_page.click_login()
    
    login_page.click_recovery()
