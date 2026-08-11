import allure
from pages.base_page import BasePageHelper
from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PHONE_BUTTON = (By.ID, "recovery-phone-btn"), "phone number button"
    EMAIL_BUTTON = (By.ID, "recovery-email-btn"), "email button"
    SUPPORT_BUTTON = (By.ID, "support-contact-btn"), "contact support button"
    QR_CODE  = (By.ID, "qr-image"), "qr code button"


class RecoveryPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)

        with allure.step("Checking the correcting recover page loading"):
            self.attach_screenshot()