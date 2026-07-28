import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper


### ---------- BASIC HELP PAGE ---------- ###
class LoginToolbarLocators:
    """Locators have the following structure::

        LOCATOR_NAME = (By.METHOD, "selector"), "element name"
    """

    OK_LOGO_BUTTON_TOOLBAR = (By.XPATH, "//*[@data-l='t,logo']//div"), "'logo'"
    SEARCH_INPUT_TOOLBAR = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-search-input']"), "search input"
    SEARCH_BUTTON_TOOLBAR = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-searchButton']"), "search button"
    VK_SERVICES_BUTTON = (By.XPATH, "//*[@aria-label='Сервисы VK']"), "'VK Services' button"

    ## VK SERVICES
    MORE_BUTTON_VK_SERVICES_MENU = (By.XPATH, "//*[@data-l='t,more']"), "'more' button"


class ToolbarWithSearchBar(BasePageHelper):

    def check_toolbar(self):
        self.find_element(LoginToolbarLocators.OK_LOGO_BUTTON_TOOLBAR)
        self.find_element(LoginToolbarLocators.SEARCH_INPUT_TOOLBAR)
        self.find_element(LoginToolbarLocators.SEARCH_BUTTON_TOOLBAR)
        self.find_element(LoginToolbarLocators.VK_SERVICES_BUTTON)

        with allure.step("Checking the correcting page toolbar loading"):
            self.attach_screenshot()

    def input_text_in_searchbar(self, text):
        self.input_text(LoginToolbarLocators.SEARCH_INPUT_TOOLBAR, text)

    def click_vk_services_button(self):
        self.click_element(LoginToolbarLocators.VK_SERVICES_BUTTON)

    def click_more_button(self):
        self.click_element(LoginToolbarLocators.MORE_BUTTON_VK_SERVICES_MENU)


### ---------- REGISTRATION PAGE ---------- ###
class RegistrationToolbarLocators:

    OK_LOGO_TOOLBAR = (By.XPATH, "//header//*[@class='vkuiButton__content']")


class ToolbarWithoutSearchBar(BasePageHelper):

    def check_toolbar(self):
        self.find_element(RegistrationToolbarLocators.OK_LOGO_TOOLBAR)
        with allure.step("Checking the correcting page toolbar loading"):
            self.attach_screenshot()

    def click_logo(self):
        self.click_element(RegistrationToolbarLocators.OK_LOGO_TOOLBAR)