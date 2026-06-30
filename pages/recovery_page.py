import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PHONE_BUTTON = (By.ID, "recovery-phone-btn")
    EMAIL_BUTTON = (By.ID, "recovery-email-btn")
    SUPPORT_BUTTON = (By.ID, "support-contact-btn")
    QR_CODE  = (By.ID, "qr-image")


class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)
        with allure.step("Checking the correcting page load"):
            self.attach_screenshot()