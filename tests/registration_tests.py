import allure

from core.base_test import browser
from pages.base_page import BasePage
from pages.login_page import LoginPageHelper
from pages.registration_page import RegistrationPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://sn.rv-school.ru/"


@allure.suite("Checking the user account registration")
@allure.title("Checking the redirection to registration by phone with selection country")
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    login_page = LoginPageHelper(browser)
    login_page.click_registration()

    registration_page = RegistrationPageHelper(browser)
    registration_page.click_registration_by_phone_btn()
    registration_page.select_random_country()