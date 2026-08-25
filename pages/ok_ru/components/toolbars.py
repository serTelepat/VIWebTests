import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper


### ---------- LOGIN PAGE ---------- ###
class LoginToolbarLocators:
    """Locators have the following structure::

        LOCATOR_NAME = (By.METHOD, "selector"), "element name"
    """

    OK_LOGO_BUTTON = (By.XPATH, "//*[@data-l='t,logo']//div"), "'logo'"
    SEARCH_INPUT = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-search-input']"), "search input"
    SEARCH_BUTTON = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-searchButton']"), "search button"
    VK_SERVICES_BUTTON = (By.XPATH, "//*[@aria-label='Сервисы VK']"), "'VK Services' button"

    ## VK SERVICES
    MORE_BUTTON_VK_SERVICES_MENU = (By.XPATH, "//*[@data-l='t,more']"), "'more' button"


class LoginToolbarWithSearchBar(BasePageHelper):

    def check_toolbar(self):
        self.find_element(LoginToolbarLocators.OK_LOGO_BUTTON)
        self.find_element(LoginToolbarLocators.SEARCH_INPUT)
        self.find_element(LoginToolbarLocators.SEARCH_BUTTON)
        self.find_element(LoginToolbarLocators.VK_SERVICES_BUTTON)

        with allure.step("Checking the correcting page toolbar loading"):
            self.attach_screenshot()

    def input_text_in_searchbar(self, text):
        self.input_text(LoginToolbarLocators.SEARCH_INPUT, text)

    def click_search_button(self):
        self.click_element(LoginToolbarLocators.SEARCH_BUTTON)

    def click_vk_services_button(self):
        self.click_element(LoginToolbarLocators.VK_SERVICES_BUTTON)

    def click_more_button(self):
        self.click_element(LoginToolbarLocators.MORE_BUTTON_VK_SERVICES_MENU)


### ---------- REGISTRATION PAGE ---------- ###
class RegistrationToolbarLocators:
    """Locators have the following structure::

        LOCATOR_NAME = (By.METHOD, "selector"), "element name"
    """

    OK_LOGO_TOOLBAR = (By.XPATH, "//header//*[@class='vkuiButton__content']"), "logo"


class ToolbarWithoutSearchBar(BasePageHelper):

    def check_toolbar(self):
        self.find_element(RegistrationToolbarLocators.OK_LOGO_TOOLBAR)
        with allure.step("Checking the correcting page toolbar loading"):
            self.attach_screenshot()

    def click_logo(self):
        self.click_element(RegistrationToolbarLocators.OK_LOGO_TOOLBAR)


### ---------- HELP PAGE ---------- ###
class HelpToolbarLocators:
    """Locators have the following structure::

        LOCATOR_NAME = (By.METHOD, "selector"), "element name"
    """

    LOGO_BUTTON = (By.XPATH, "//*[@class='toolbar_logo_img']"), "logo"
    SEARCH_INPUT = (By.XPATH, "//*[@id='topPanel']//*[@data-tsid='toolbar-search-input']"), "search input"
    SEARCH_BUTTON = (By.XPATH, "//*[@class='toolbar_search_mini-button']"), "search button"
    VK_SERVICES_BUTTON = (By.XPATH, "//*[@aria-label='Сервисы VK']"), "'VK Services' button"
    LOGIN_BUTTON = (By.XPATH, "//*[@data-module='AuthLoginPopup']"), "login button"

    ## VK SERVICES
    MORE_BUTTON_VK_SERVICES_MENU = (By.XPATH, "//*[@data-l='t,more']"), "'more' button"


class HelpToolbarHelper(BasePageHelper):
    def check_toolbar(self):
        self.find_element(HelpToolbarLocators.LOGO_BUTTON)
        self.find_element(HelpToolbarLocators.SEARCH_BUTTON)
        self.find_element(HelpToolbarLocators.VK_SERVICES_BUTTON)
        self.find_element(HelpToolbarLocators.LOGIN_BUTTON)

        with allure.step("Checking the correcting page toolbar loading"):
            self.attach_screenshot()

    def click_search_button(self):
        self.click_element(HelpToolbarLocators.SEARCH_BUTTON)

    def click_vk_services_button(self):
        self.click_element(HelpToolbarLocators.VK_SERVICES_BUTTON)


