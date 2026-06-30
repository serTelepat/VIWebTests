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
        self.find_element(LoginPageLocators.VISIBLE_PASSWORD_FIELD)

        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.FORGET_ACCOUNT_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)

        self.find_element(LoginPageLocators.VK_O_AUTH)
        self.find_element(LoginPageLocators.MAIL_O_AUTH)
        self.find_element(LoginPageLocators.GOOGLE_O_AUTH)
        self.find_element(LoginPageLocators.YANDEX_O_AUTH)
        self.find_element(LoginPageLocators.APPLE_O_AUTH)
        with allure.step("Checking the correcting page load"):
            self.attach_screenshot()

    @allure.step("Clicking the button \"Войти\"")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Getting error text")
    def get_error_text(self, type_error):
        if type_error == "empty login":
            element_text = self.find_element(LoginPageLocators.EMPTY_LOGIN)
        elif type_error == "empty password":
            element_text = self.find_element(LoginPageLocators.EMPTY_PASSWORD)
        else:
            element_text = self.find_element(LoginPageLocators.INCORRECT_LOGIN_OR_PASSWORD)

        self.attach_screenshot()
        return element_text.text

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
        self.find_element(LoginPageLocators.RECOVER_BUTTON).click()

    @allure.step("Log in until the recovery form appears")
    def click_login_until_appearing_recover_form(self, time_for_recover_form):
        toggle = False
        while not toggle:
            try:
                self.attach_screenshot()
                self.find_element(LoginPageLocators.LOGIN_BUTTON).click()
                self.find_element(LoginPageLocators.RECOVER_BUTTON, time_for_recover_form)
                toggle = True
            except Exception:
                toggle = False
                continue
