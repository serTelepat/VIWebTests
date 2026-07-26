import allure

from pages.base_page import BasePageHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HelpPageLocators:

    ### ---------- BASIC HELP PAGE ---------- ###
    # # TOOLBAR
    # LOGIN_BUTTON = (By.XPATH, "//*[@data-module='AuthLoginPopup']")
    # VK_SERVICES_BUTTON = (By.XPATH, "//*[@aria-label='Сервисы VK']")
    # SEARCH_BUTTON = (By.XPATH, "//*[@class='toolbar_search_mini-button']")

    # MAIN SEARCH BLOCK
    SEARCH_BTN_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='button_to_search']")
    SEARCH_BAR_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='help_search_input']")

    ACCOUNT_RECOVER_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='восстановить профиль']")
    PASSWORD_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='пароль']")
    UNLOCKING_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='разблокировать']")
    PHOTO_WITH_CODE_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='фото с кодом']")
    REGISTRATION_INFO_OF_SEARCH_BLCK = (By.XPATH, "//*[text()='регистрация']")

    # HELP PAGE BREADCRUMBS
    HELP_TAB = (By.XPATH, "//*[@href='/help']//span")

    # MAIN BLOCK
    TODAY_WIDGET = (By.XPATH, "//*[@href='/help/segodnya-aktualno']")
    REGISTRATION_WIDGET = (By.XPATH, "//*[@href='/help/registraciya']")
    MY_PROFILE_WIDGET = (By.XPATH, "//*[@href='/help/moi-profil']")
    COMMUNICATION_WIDGET = (By.XPATH, "//*[@href='/help/obshchenie']")
    PROFILE_ACCESS_WIDGET = (By.XPATH, "//*[@href='/help/dostup-k-profilu']")
    SECURITY_WIDGET = (By.XPATH, "//*[@href='/help/bezopasnost']")
    GROUPS_WIDGET = (By.XPATH, "//*[@href='/help/gruppy']")
    PAID_FUNCTIONAL_WIDGET = (By.XPATH, "//*[@href='/help/platnye-funkcii']")
    VIOLATIONS_AND_SPAM_WIDGET = (By.XPATH, "//*[@href='/help/narusheniya-i-spam']")
    GAMES_AND_APPLICATIONS_WIDGET = (By.XPATH, "//*[@href='/help/igry-i-prilojeniya']")
    OTHER_SERVICES_WIDGET = (By.XPATH,  "//*[@href='/help/drugie-servisy']")
    USEFUL_INFO_WIDGET = (By.XPATH, "//*[@href='/help/poleznaya-informaciya']")
    ADVERTISEMENT_CABINET_WIDGET = (By.XPATH, "//*[@href='/help/reklamnyi-kabinet']")


class HelpPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        # self.find_element(HelpPageLocators.LOGIN_BUTTON)
        # self.find_element(HelpPageLocators.VK_SERVICES_BUTTON)
        # self.find_element(HelpPageLocators.SEARCH_BUTTON)

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

        with allure.step("Checking the correcting help page load"):
            self.attach_screenshot()

    @allure.step("Scroll to the page element and click on it")
    def scroll_to_item_and_click(self, locator):
        scroll_element = self.find_element(locator)
        with allure.step(f"Scroll to the element"):
            ActionChains(self.driver).scroll_to_element(scroll_element).perform()
            self.attach_screenshot()
        scroll_element.click()
