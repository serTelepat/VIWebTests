import allure

from core.base_test import browser
from pages.base_page import BasePageHelper
from pages.sn_rv_school.login_page import LoginPageHelper
from pages.sn_rv_school.registration_page import RegistrationPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://sn.rv-school.ru/"


@allure.suite("Checking the user account registration")
@allure.title("Checking the redirection to registration by phone with selection country")
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    login_page.click_registration()

    registration_page = RegistrationPageHelper(browser)
    registration_page.click_registration_by_phone_btn()
    selected_country_text = registration_page.select_random_country()
    actual_country_text = registration_page.get_phone_field_value()
    assert selected_country_text == actual_country_text, "The displayed country does not match the selected one."