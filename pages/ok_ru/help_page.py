import allure

from pages.base_page import BasePageHelper
from pages.ok_ru.components.toolbars import HelpToolbarHelper
from selenium.webdriver.common.by import By


class HelpPageLocators:

    # MAIN SEARCH BLOCK
    SEARCH_BTN_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='button_to_search']"), "search button"
    SEARCH_BAR_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='help_search_input']"), "search bar"

    ACCOUNT_RECOVER_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='восстановить профиль']"), "account recover info"
    PASSWORD_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='пароль']"), "password info"
    UNLOCKING_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='разблокировать']"), "unlocking info"
    PHOTO_WITH_CODE_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='фото с кодом']"), "photo with code info"
    REGISTRATION_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='регистрация']"), "registration info"

    # HELP PAGE BREADCRUMBS
    HELP_TAB = (By.XPATH, "//*[@href='/help']//span"), "help tab"

    # MAIN BLOCK
    TODAY_WIDGET = (By.XPATH, "//*[@href='/help/segodnya-aktualno']"), "'today' widget"
    REGISTRATION_WIDGET = (By.XPATH, "//*[@href='/help/registraciya']"), "'registration' widget"
    MY_PROFILE_WIDGET = (By.XPATH, "//*[@href='/help/moi-profil']"), "'my profile' widget"
    COMMUNICATION_WIDGET = (By.XPATH, "//*[@href='/help/obshchenie']"), "'communication' widget"
    PROFILE_ACCESS_WIDGET = (By.XPATH, "//*[@href='/help/dostup-k-profilu']"), "'profile access' widget"
    SECURITY_WIDGET = (By.XPATH, "//*[@href='/help/bezopasnost']"), "'security' widget"
    GROUPS_WIDGET = (By.XPATH, "//*[@href='/help/gruppy']"), "'groups' widget"
    PAID_FUNCTIONAL_WIDGET = (By.XPATH, "//*[@href='/help/platnye-funkcii']"), "'paid functional' widget"
    VIOLATIONS_AND_SPAM_WIDGET = (By.XPATH, "//*[@href='/help/narusheniya-i-spam']"), "'violations and spam' widget'"
    GAMES_AND_APPLICATIONS_WIDGET = (By.XPATH, "//*[@href='/help/igry-i-prilojeniya']"), "'games and applications' widget"
    OTHER_SERVICES_WIDGET = (By.XPATH,  "//*[@href='/help/drugie-servisy']"), "'other services' widget"
    USEFUL_INFO_WIDGET = (By.XPATH, "//*[@href='/help/poleznaya-informaciya']"), "'useful info' widget"
    ADVERTISEMENT_CABINET_WIDGET = (By.XPATH, "//*[@href='/help/reklamnyi-kabinet']"), "'advertisement cabinet' widget"


class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.toolbar = HelpToolbarHelper(driver)
        self.toolbar.check_toolbar()
        self.check_page()

    def check_page(self):
        self.find_element(HelpPageLocators.SEARCH_BTN_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.SEARCH_BAR_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.ACCOUNT_RECOVER_INFO_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.PASSWORD_INFO_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.UNLOCKING_INFO_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.PHOTO_WITH_CODE_INFO_OF_SEARCH_BLCK)
        self.find_element(HelpPageLocators.REGISTRATION_INFO_OF_SEARCH_BLCK)

        self.find_element(HelpPageLocators.HELP_TAB)
        self.find_element(HelpPageLocators.TODAY_WIDGET)
        self.find_element(HelpPageLocators.REGISTRATION_WIDGET)
        self.find_element(HelpPageLocators.MY_PROFILE_WIDGET)
        self.find_element(HelpPageLocators.COMMUNICATION_WIDGET)
        self.find_element(HelpPageLocators.PROFILE_ACCESS_WIDGET)
        self.find_element(HelpPageLocators.SECURITY_WIDGET)
        self.find_element(HelpPageLocators.GROUPS_WIDGET)
        self.find_element(HelpPageLocators.PAID_FUNCTIONAL_WIDGET)
        self.find_element(HelpPageLocators.VIOLATIONS_AND_SPAM_WIDGET)
        self.find_element(HelpPageLocators.GAMES_AND_APPLICATIONS_WIDGET)
        self.find_element(HelpPageLocators.OTHER_SERVICES_WIDGET)
        self.find_element(HelpPageLocators.USEFUL_INFO_WIDGET)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET_WIDGET)

        with allure.step("Checking the correcting help page loading"):
            self.attach_screenshot()

    @allure.step("Scroll to the page element and click on it")
    def scroll_to_item_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_element(locator)
