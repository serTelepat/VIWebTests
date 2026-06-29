import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:

    ### ---------- BASIC LOGIN FORM ---------- ###
    # TABS
    LOGIN_TAB = (By.XPATH, "//*[text()=\"Вход\"]")
    QR_CODE_TAB = (By.XPATH, "//*[text()=\"QR-код\"]")

    # FIELDS AND THEIR BUTTONS
    LOGIN_FIELD = (By.ID, "field_email")
    PASSWORD_FIELD = (By.ID, "field_password")
    VISIBLE_PASSWORD_FIELD = (By.XPATH, "//*[@class=\"vkuiFormField__scrollContainer\"]//button")

    # BUTTONS UNDER FIELDS
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id=\"enter-action\"]")
    LOGIN_QR_CODE_BUTTON = (By.XPATH, "//button[@label=\"Войти по QR-коду\"]")
    FORGET_ACCOUNT_BUTTON = (By.XPATH, "//button[@aria-label=\"Не получается войти?\"]")
    REGISTRATION_BUTTON = (By.XPATH, "//div[contains(@class, \"LoginFormMain-module__bottom\")]//button")

    # OAUTH LINKS
    VK_O_AUTH = (By.XPATH, "//*[@data-l=\"t,vkc\"]//i")
    MAIL_O_AUTH = (By.XPATH, "//*[@data-l=\"t,mailru\"]//i")
    GOOGLE_O_AUTH =  (By.XPATH, "//*[@data-l=\"t,google\"]//i")
    YANDEX_O_AUTH = (By.XPATH, "//*[@data-l=\"t,yandex\"]//i")
    APPLE_O_AUTH = (By.XPATH, "//*[@data-l=\"t,apple\"]//i")

    # ERROR TEXTS
    EMPTY_LOGIN = (By.XPATH, "//*[text()=\"Введите логин\"]")
    EMPTY_PASSWORD = (By.XPATH, "//*[text()=\"Введите пароль\"]")
    INCORRECT_LOGIN_OR_PASSWORD = (By.XPATH, "//*[text()=\"Неправильно указан логин и/или пароль\"]")


    ### ---------- ADDITIONAL RESTORE PROFILE FORM ---------- ###
    # BUTTONS
    RECOVER_BUTTON = (By.XPATH, "//*[@href=\"https://ok.ru/dk?st.cmd=anonymRecoveryStart\"]")
    CANCEL_RECOVER_BUTTON = (By.XPATH, "//*[@role=\"group\"]//button")


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
