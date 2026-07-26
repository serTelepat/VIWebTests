import allure
from pages.base_page import BasePageHelper
from selenium.webdriver.common.by import By


class VKServicesLocators:
    VK_LOGO_HEADER = (By.XPATH,  "//header//*[@id='header-logo']")

class VKServicesHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(VKServicesLocators.VK_LOGO_HEADER)
        with allure.step("Checking the correcting VK Services page loading"):
            self.attach_screenshot()