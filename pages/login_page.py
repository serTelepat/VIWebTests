from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:

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


class LoginPageHelper(BasePage):
    pass