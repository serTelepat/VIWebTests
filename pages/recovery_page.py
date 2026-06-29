import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, "//*[@data-l=\"t,phone\"]")
    EMAIL_BUTTON = (By.XPATH, "//*[@data-l=\"t,email\"]")
    QR_CODE  = (By.XPATH, "//*[@class=\"qr_code_image\"]")
    SUPPORT_BUTTON = (By.XPATH, "//*[@data-l=\"t,support\"]")


class RecoveryPageHelpers(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(*RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(*RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(*RecoveryPageLocators.QR_CODE)
        self.find_element(*RecoveryPageLocators.SUPPORT_BUTTON)