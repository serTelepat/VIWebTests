import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f"{locator} element not found")

    def find_element_to_clickable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator),
                                                      message=f"{locator} element not clickable")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator),
                                                      message=f"{locator} elements not found")

    @allure.step("Opening the page")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot", allure.attachment_type.PNG)