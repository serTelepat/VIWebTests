import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePageHelper
from pages.ok_ru.components.toolbars import HelpToolbarHelper


class AdvertisementPageLocators:

    ### ---------- BASIC ADVERTISEMENT PROFILE PAGE ---------- ###
    # MAIN SEARCH BLOCK
    SEARCH_BTN_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='button_to_search']"), "search button"
    SEARCH_BAR_OF_SEARCH_BLCK = (By.XPATH, "//*[@data-tsid='help_search_input']"), "search bar"

    # HELP PAGE BREADCRUMBS
    HELP_TAB = (By.XPATH, "//*[@href='/help']//span"), "help tab"
    ADVERTISEMENT_CABINET_TAB = (By.XPATH, "//*[@href='/help/reklamnyi-kabinet']//span"), "'advertisement cabinet' tab"

    TEXT_ADVERTISEMENT_CABINET_TAB = (By.XPATH, "//span[text()='Рекламный кабинет']"), "'advertisement cabinet' tab"

    # MAIN ADVERTISEMENT PAGE BLOCK
    GET_LINK_BUTTON = (By.XPATH, "//*[@class='help_app_link-toggler']"), "'get link' link"

    COMMON_QUESTIONS = (By.XPATH, "//*[@href='/help/obshchie-voprosy-pro-reklamnyi-kabinet']"), "'common questions' tab"
    CREATING_PROMOTION = (By.XPATH, "//*[@href='/help/sozdanie-prodvijeniya']"), "'creating promotion' tab"
    PROMOTION_MANAGEMENT = (By.XPATH, "//*[@href='/help/upravlenie-prodvijeniem']"), "'promotion management' tab"
    STATISTICS = (By.XPATH, "//*[@href='/help/statistika']"), "'statistics' tab"
    ADVERTISEMENT_RULES = (By.XPATH, "//*[@href='/help/pravila-razmeshcheniya-reklamy']"), "'advertisement rules' tab"
    PAYMENT = (By.XPATH, "//*[@href='/help/oplata']"), "'payment' tab"

    # POPULAR QUESTIONS BLOCK
    OLD_ACCOUNT_FINDING = (
        By.XPATH,
        "//*[@href='/help/kak-naiti-svou-staruu-stranicu-v-odnoklassnikah']"
    ), "'old account finding' tab"

    APP_DISAPPEARS_FROM_APP_STORE = (
        By.XPATH,
        "//*[@href='/help/chto-delat-esli-iz-app-store-propalo-prilojenie-odnoklassniki']"
    ), "'app disappears in app store' tab"

    HOW_TO_TURN_OFF_ADBLOCK_IN_OPERA = (
        By.XPATH,
        "//*[@href='/help/kak-otkluchit-blokirovshchiki-reklamy-v-opera']"
    ), "'how to turn off adblock in opera' tab"

    HOW_TO_TURN_OFF_ADBLOCK_IN_CHROME = (
        By.XPATH,
        "//*[@href='/help/kak-otkluchit-blokirovshchiki-reklamy-v-chrome']"
    ), "'how to turn off adblock in chrome' tab"

    HOW_TO_CREATE_ACCOUNT = (
        By.XPATH,
        "//*[@href='/help/kak-sozdat-stranicu-v-odnoklassnikah']"
    ), "'how to create account' tab"

    HOW_TO_RECOVER_ACCOUNT = (
        By.XPATH,
        "//*[@href='/help/kak-vosstanovit-stranicu-v-odnoklassnikah']"
    ), "'how to recover account' tab"

    WHAT_IS_LICENSE_AGREEMENT_AND_WHERE_IT = (
        By.XPATH,
        "//*[@href='/help/chto-takoe-licenzionnoe-soglashenie-i-gde-ego-naiti']"
    ), "'what is license agreement and where' tab"

    HOW_TO_ACCESS_APP_WITHOUT_REGISTRATION = (
        By.XPATH,
        "//*[@href='/help/kak-zaiti-v-odnoklassniki-bez-registracii']"
    ), "'how to access app without registration' tab"

    HOW_TO_CONTACT_SUPPORT = (
        By.XPATH,
        "//*[@href='/help/kak-napisat-v-slujbu-podderjki-odnoklassnikov']"
    ), "'how to contact support' tab"

    WHAT_IS_NEED_TO_USE_CALLS_SERVICE = (
        By.XPATH,
        "//*[@href='/help/chto-nujno-dlya-togo-chtoby-vospolzovatsya-servisom-zvonki']"
    ), "'what's need to use calls service' tab"

    HOW_TO_RECOVER_DELETED_PROFILE = (
        By.XPATH,
        "//*[@href='/help/kak-vosstanovit-udalennyi-profil']"
    ), "'how to recover deleted profile' tab"

    HOW_TO_TURN_OFF_ADBLOCK_IN_YANDEX = (
        By.XPATH,
        "//*[@href='/help/kak-otkluchit-blokirovshchiki-reklamy-v-yandex-brauzere']"
    ), "'how to turn off adblock in yandex' tab"

    WRITE_TO_TECH_SUPPORT = (By.XPATH, "//*[@data-tsid='write-us-button']"), "'write to tech support' button"


class AdvertisementPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.toolbar = HelpToolbarHelper(driver)
        self.toolbar.check_toolbar()
        self.check_page()

    def check_page(self):
        self.find_element(AdvertisementPageLocators.SEARCH_BTN_OF_SEARCH_BLCK)
        self.find_element(AdvertisementPageLocators.SEARCH_BAR_OF_SEARCH_BLCK)

        self.find_element(AdvertisementPageLocators.HELP_TAB)
        self.find_element(AdvertisementPageLocators.TEXT_ADVERTISEMENT_CABINET_TAB)

        self.find_element(AdvertisementPageLocators.GET_LINK_BUTTON)
        self.find_element(AdvertisementPageLocators.COMMON_QUESTIONS)
        self.find_element(AdvertisementPageLocators.CREATING_PROMOTION)
        self.find_element(AdvertisementPageLocators.PROMOTION_MANAGEMENT)
        self.find_element(AdvertisementPageLocators.STATISTICS)
        self.find_element(AdvertisementPageLocators.ADVERTISEMENT_RULES)
        self.find_element(AdvertisementPageLocators.PAYMENT)

        self.find_element(AdvertisementPageLocators.OLD_ACCOUNT_FINDING)
        self.find_element(AdvertisementPageLocators.APP_DISAPPEARS_FROM_APP_STORE)
        self.find_element(AdvertisementPageLocators.HOW_TO_TURN_OFF_ADBLOCK_IN_OPERA)
        self.find_element(AdvertisementPageLocators.HOW_TO_TURN_OFF_ADBLOCK_IN_CHROME)
        self.find_element(AdvertisementPageLocators.HOW_TO_CREATE_ACCOUNT)
        self.find_element(AdvertisementPageLocators.HOW_TO_RECOVER_ACCOUNT)
        self.find_element(AdvertisementPageLocators.WHAT_IS_LICENSE_AGREEMENT_AND_WHERE_IT)
        self.find_element(AdvertisementPageLocators.HOW_TO_ACCESS_APP_WITHOUT_REGISTRATION)
        self.find_element(AdvertisementPageLocators.HOW_TO_CONTACT_SUPPORT)
        self.find_element(AdvertisementPageLocators.WHAT_IS_NEED_TO_USE_CALLS_SERVICE)
        self.find_element(AdvertisementPageLocators.HOW_TO_RECOVER_DELETED_PROFILE)
        self.find_element(AdvertisementPageLocators.HOW_TO_TURN_OFF_ADBLOCK_IN_YANDEX)
        self.find_element(AdvertisementPageLocators.WRITE_TO_TECH_SUPPORT)

        with allure.step("Checking the correcting advertisement profile help page loading"):
            self.attach_screenshot()