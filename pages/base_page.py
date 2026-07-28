import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageHelper:
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

    @allure.step("Opening the {url} page")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot", allure.attachment_type.PNG)

    @allure.step("Click the {element_locator[1]}")
    def click_element(self, element_locator):
        self.find_element(element_locator[0]).click()
        self.attach_screenshot()

    @allure.step("Input the '{text}' text in the {element_locator[1]}")
    def input_text(self, element_locator, text):
        self.find_element(element_locator[0]).send_keys(text)
        self.attach_screenshot()

    @allure.step("Get window hash for switching")
    def get_window_id(self, index_page):
        return self.driver.window_handles[index_page]

    @allure.step("Switching the browser window")
    def switch_current_window(self, window_id):
        self.driver.switch_to.window(window_id)
