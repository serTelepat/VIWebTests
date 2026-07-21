import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:

    ### ---------- BASIC LOGIN FORM ---------- ###
    # TABS
    LOGIN_TAB = (By.ID, "tabLogin")
    QR_CODE_TAB = (By.ID, "tabQr")

    # FIELDS AND THEIR BUTTONS
    LOGIN_FIELD = (By.ID, "login-phone-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    # VISIBLE_PASSWORD_FIELD = (By.ID, "")

    # BUTTONS UNDER FIELDS
    LOGIN_BUTTON = (By.ID, "login-submit-btn")
    FORGET_PASSWORD_BUTTON = (By.ID, "forgot-password-link")

    # BUTTONS LEFT FORM
    LOGIN_BUTTON_LEFT = (By.ID,  "hero-login-btn")
    REGISTRATION_BUTTON_LEFT = (By.ID, "hero-register-btn")

    # ERROR TEXTS
    ERROR_TEXT_FORM = (By.ID, "login-error")

    ### ---------- ADDITIONAL RESTORE PROFILE FORM ---------- ###
    # BUTTONS
    RECOVER_BUTTON_RECOVER_FORM = (By.ID, "lockout-recover-btn")
    CANCEL_RECOVER_BUTTON_RECOVER_FORM = (By.ID, "lockout-cancel-btn")
    REGISTER_BUTTON_RECOVER_FORM = (By.ID, "lockout-register-btn")


class LoginPageHelper(BasePage):
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

        with allure.step("Checking the correcting login page load"):
            self.attach_screenshot()

    @allure.step("Clicking the button \"Войти\"")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Getting error text")
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT_FORM).text

    @allure.step("Entering the login")
    def enter_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Entering the password")
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Go to recovery page")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVER_BUTTON_RECOVER_FORM).click()

    @allure.step("Log in until the recovery form appears")
    def click_login_until_appearing_recover_form(self):
        for attempt in range(3):
            self.attach_screenshot()
            self.find_element_to_clickable(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Click the registration button")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON_LEFT).click()