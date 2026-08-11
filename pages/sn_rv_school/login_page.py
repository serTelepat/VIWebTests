import allure
from pages.base_page import BasePageHelper
from selenium.webdriver.common.by import By


class LoginPageLocators:

    ### ---------- BASIC LOGIN FORM ---------- ###
    # TABS
    LOGIN_TAB = (By.ID, "tabLogin"), "login tab"
    QR_CODE_TAB = (By.ID, "tabQr"), "qr code tab"

    # FIELDS AND THEIR BUTTONS
    LOGIN_FIELD = (By.ID, "login-phone-email"), "login field"
    PASSWORD_FIELD = (By.ID, "login-password"), "password field"
    # VISIBLE_PASSWORD_FIELD = (By.ID, "")

    # BUTTONS UNDER FIELDS
    LOGIN_BUTTON = (By.ID, "login-submit-btn"), "login button"
    FORGET_PASSWORD_BUTTON = (By.ID, "forgot-password-link"), "forgot password link"

    # BUTTONS LEFT FORM
    LOGIN_BUTTON_LEFT = (By.ID,  "hero-login-btn"), "left login button"
    REGISTRATION_BUTTON_LEFT = (By.ID, "hero-register-btn"), "left register button"

    # ERROR TEXTS
    ERROR_TEXT_FORM = (By.ID, "login-error"), "error label"

    ### ---------- ADDITIONAL RESTORE PROFILE FORM ---------- ###
    # BUTTONS
    RECOVER_BUTTON_RECOVER_FORM = (By.ID, "lockout-recover-btn"), "recover button"
    CANCEL_RECOVER_BUTTON_RECOVER_FORM = (By.ID, "lockout-cancel-btn"), "cancel button"
    REGISTER_BUTTON_RECOVER_FORM = (By.ID, "lockout-register-btn"), "'registration' button"


class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_CODE_TAB)

        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        # self.find_element(LoginPageLocators.VISIBLE_PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGET_PASSWORD_BUTTON)

        self.find_element(LoginPageLocators.LOGIN_BUTTON_LEFT)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_LEFT)

        with allure.step("Checking the correcting login page loading"):
            self.attach_screenshot()

    def click_login(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Getting error text")
    def get_error_text(self):
        return self.get_text(LoginPageLocators.ERROR_TEXT_FORM)

    @allure.step("Entering the login")
    def enter_login(self, login):
        self.input_text(LoginPageLocators.LOGIN_FIELD, login)

    @allure.step("Entering the password")
    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step("Go to recovery page")
    def click_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_BUTTON_RECOVER_FORM)

    @allure.step("Log in until the recovery form appears")
    def click_login_until_appearing_recover_form(self):
        for attempt in range(3):
            self.attach_screenshot()
            self.click_clickable_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Click the registration button")
    def click_registration(self):
        self.click_element(LoginPageLocators.REGISTRATION_BUTTON_LEFT)