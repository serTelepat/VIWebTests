import allure

from core.base_test import browser
from pages.base_page import BasePageHelper
from pages.ok_ru.login_page import LoginPageHelper
from pages.vk.vk_services_page import VKServicesHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://ok.ru/"


@allure.suite("Checking the toolbar")
@allure.title("Checking the transition between login and VK services pages")
def test_open_vk_services(browser):
    base_page = BasePageHelper(browser)
    base_page.get_url(BASE_URL)

    login_page = LoginPageHelper(browser)
    first_focus_page = login_page.get_window_id(0)
    login_page.go_to_vk_services_page()

    new_focus_page = login_page.get_window_id(1)
    login_page.switch_current_window(new_focus_page)
    vk_services_page = VKServicesHelper(browser)
    vk_services_page.switch_current_window(first_focus_page)

    LoginPageHelper(browser)