import allure
import random

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    ### ---------- REGISTRATION FORM BY EMAIL AND PHONE ---------- ###
    FIRST_LAST_NAMES_FIELD = (By.ID, "display-name")
    LOGIN_FIELD = (By.ID, "username")
    EMAIL_FIELD = (By.ID, "email")
    PHONE_FIELD_BY_EMAIL = (By.ID, "phone")
    PASSWORD_FIELD = (By.ID, "register-password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "confirm-password")

    REGISTER_BTN_BY_EMAIL = (By.ID, "register-submit-btn")
    REGISTER_BY_PHONE_BTN = (By.ID, "register-phone-toggle")
    LOGIN_BTN = (By.ID, "login-link-anchor")


    ### ---------- REGISTRATION FORM BY PHONE ---------- ###
    COUNTRY_LIST = (By.ID, "phone-country-select")
    COUNTRY_ITEM = (By.XPATH, "//*[contains(@data-test-id, 'phone-country-option')]")

    PHONE_FIELD = (By.ID, "phone-number-input")
    GET_CODE_BTN = (By.ID, "phone-send-code-btn")
    CANCEL_BTN = (By.ID, "phone-cancel-btn")

    SELECTED_COUNTRY_OPTION = (By.CSS_SELECTOR, "select[data-test-id='phone-country-select'] option:checked")


class RegistrationPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RegistrationPageLocators.FIRST_LAST_NAMES_FIELD)
        self.find_element(RegistrationPageLocators.LOGIN_FIELD)
        self.find_element(RegistrationPageLocators.EMAIL_FIELD)
        self.find_element(RegistrationPageLocators.PHONE_FIELD_BY_EMAIL)
        self.find_element(RegistrationPageLocators.PASSWORD_FIELD)
        self.find_element(RegistrationPageLocators.CONFIRM_PASSWORD_FIELD)

        self.find_element(RegistrationPageLocators.REGISTER_BTN_BY_EMAIL)
        self.find_element(RegistrationPageLocators.REGISTER_BY_PHONE_BTN)
        self.find_element(RegistrationPageLocators.LOGIN_BTN)

        with allure.step("Checking the correcting registration page load"):
            self.attach_screenshot()

    def check_page_for_phone_registration_form(self):
        self.find_element(RegistrationPageLocators.COUNTRY_LIST)
        self.find_element(RegistrationPageLocators.PHONE_FIELD)

        self.find_element(RegistrationPageLocators.GET_CODE_BTN)
        self.find_element(RegistrationPageLocators.CANCEL_BTN)
        self.find_element(RegistrationPageLocators.LOGIN_BTN)

        with allure.step("Checking the correcting page updating"):
            self.attach_screenshot()

    @allure.step("Click the button of registration by phone")
    def click_registration_by_phone_btn(self):
        self.find_element(RegistrationPageLocators.REGISTER_BY_PHONE_BTN).click()
        self.check_page_for_phone_registration_form()

    @allure.step("Select random country from list")
    def select_random_country(self):
        random_number = random.randint(0, 39)
        with allure.step("Open the country list"):
            self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
            self.attach_screenshot()

        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        with allure.step("Click the random country in list"):
            country_text = country_items[random_number]
            country_items[random_number].click()
            self.attach_screenshot()

        return country_text.get_attribute("text")

    def get_phone_field_value(self):
        value = self.find_element(RegistrationPageLocators.SELECTED_COUNTRY_OPTION)
        return value.text
