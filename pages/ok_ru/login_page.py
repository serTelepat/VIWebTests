import allure

from pages.base_page import BasePageHelper
from pages.ok_ru.components.toolbars import LoginToolbarWithSearchBar
from selenium.webdriver.common.by import By


class LoginPageLocators:

    ### ---------- BASIC LOGIN FORM OF ok.ru ---------- ###
    # TABS
    LOGIN_TAB = (By.XPATH, "//*[@data-l='t,login_tab']"), "login tab"
    QR_CODE_TAB = (By.XPATH, "//*[@data-l='t,qr_tab']"), "qr code tab"

    # FIELDS AND THEIR BUTTONS
    LOGIN_FIELD = (By.ID, "field_email"), "login field"
    PASSWORD_FIELD = (By.ID, "field_password"), "password field"

    VISIBLE_PASSWORD_BUTTON = (
        By.XPATH,
        "//*[@class='vkuiFormField__scrollContainer']//button"
    ), "password visible button"

    # BUTTONS UNDER FIELDS
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='enter-action']"), "login button"
    LOGIN_QR_CODE_BUTTON = (By.XPATH, "//button[@label='Войти по QR-коду']"), "qrcode login button"
    FORGET_ACCOUNT_BUTTON = (By.XPATH, "//button[@aria-label='Не получается войти?']"), "forget account button"

    REGISTRATION_BUTTON = (
        By.XPATH,
        "//div[contains(@class, \"LoginFormMain-module__bottom\")]//button"
    ), "registration button"

    # OAUTH LINKS
    VK_O_AUTH = (By.XPATH, "//*[@data-l=\"t,vkc\"]//i"), "'vk authorization' button"
    MAIL_O_AUTH = (By.XPATH, "//*[@data-l=\"t,mailru\"]//i"), "'mail authorization' button"
    GOOGLE_O_AUTH =  (By.XPATH, "//*[@data-l=\"t,google\"]//i"), "'google authorization' button"
    YANDEX_O_AUTH = (By.XPATH, "//*[@data-l=\"t,yandex\"]//i"), "'yandex authorization' button"
    APPLE_O_AUTH = (By.XPATH, "//*[@data-l=\"t,apple\"]//i"), "'apple authorization' button"

    ERROR_TEXT_LABEL = (
        By.XPATH,
        "//span[contains(@class, 'LoginForm-module__error')][normalize-space(text()) != '']"
    ), "error label"

    ### ---------- RECOVER LOGIN FORM OF ok.ru ---------- ###
    RECOVER_BUTTON = (By.XPATH, "//*[@href='https://ok.ru/dk?st.cmd=anonymRecoveryStart']"), "recover button"

    CANCEL_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButtonGroup__host')]//button[contains(@class, 'vkuiInternalTappable')]"
    ), "cancel button"


class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.toolbar = LoginToolbarWithSearchBar(driver)
        self.toolbar.check_toolbar()
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_CODE_TAB)

        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.VISIBLE_PASSWORD_BUTTON)

        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.FORGET_ACCOUNT_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)

        self.find_element(LoginPageLocators.VK_O_AUTH)
        self.find_element(LoginPageLocators.MAIL_O_AUTH)
        self.find_element(LoginPageLocators.GOOGLE_O_AUTH)
        self.find_element(LoginPageLocators.YANDEX_O_AUTH)
        self.find_element(LoginPageLocators.APPLE_O_AUTH)

        with allure.step("Checking the correcting ok.ru login page loading"):
            self.attach_screenshot()

    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Getting error text")
    def get_error_text(self):
        return self.get_text(LoginPageLocators.ERROR_TEXT_LABEL)

    @allure.step("Entering the login")
    def enter_login(self, login):
        self.input_text(LoginPageLocators.LOGIN_FIELD, login)

    @allure.step("Entering the password")
    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Going to recovery page")
    def click_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_BUTTON)

    @allure.step("Logging until the recovery form appears")
    def click_login_until_appearing_recover_form(self):
        for attempt in range(3):
            self.attach_screenshot()
            self.click_clickable_element(LoginPageLocators.LOGIN_BUTTON)

    def click_registration(self):
        self.click_element(LoginPageLocators.RECOVER_BUTTON)

    def go_to_vk_services_page(self):
        self.toolbar.click_vk_services_button()
        self.toolbar.click_more_button()
