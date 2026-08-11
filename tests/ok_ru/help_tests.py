import allure

from core.base_test import browser
from pages.base_page import BasePageHelper
from pages.ok_ru.help_page import HelpPageLocators, HelpPageHelper
from pages.ok_ru.advertisement_cabinet_help_page import AdvertisementPageHelper


#### ------- CONSTANTS ------- ####
BASE_URL = "https://ok.ru/help"


@allure.suite("Checking the help page")
@allure.title("Checking the scrolling the help page and redirection to advertisement page")
def test_scrolling_and_redirection_to_advertisement_page(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    help_page = HelpPageHelper(browser)
    help_page.scroll_to_item_and_click(HelpPageLocators.ADVERTISEMENT_CABINET_WIDGET)
    AdvertisementPageHelper(browser)

