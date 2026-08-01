import allure

from utils.allure_steps import allure_locator_step

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element_locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(element_locator[0]),
                                                      message=f"{element_locator[1]} element not found")

    def find_element_to_clickable(self, element_locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(element_locator[0]),
                                                      message=f"{element_locator[1]} element not clickable")

    def find_elements(self, element_locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(element_locator[0]),
                                                      message=f"{element_locator[1]} elements not found")

    @allure.step("Opening the {url} page")
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "Screenshot", allure.attachment_type.PNG)

    @allure_locator_step("Click the {element_name}")
    def click_element(self, element_locator):
        self.find_element(element_locator).click()
        self.attach_screenshot()

    def click_web_element(self, web_element):
        """Use when there is no redirection to other page"""
        web_element.click()
        self.attach_screenshot()

    @allure_locator_step("Click the {element_name}")
    def click_clickable_element(self, element_locator):
        self.find_element_to_clickable(element_locator).click()
        self.attach_screenshot()

    @allure_locator_step("Inputting the '{text}' text in the {element_name}")
    def input_text(self, element_locator, text):
        self.find_element(element_locator).send_keys(text)
        self.attach_screenshot()

    @allure_locator_step("Getting the text from the {element_name}")
    def get_text(self, element_locator):
        self.attach_screenshot()
        return self.find_element(element_locator).text

    @allure_locator_step("Scroll to the {element_name}")
    def scroll_to_element(self, element_locator):
        scroll_element = self.find_element(element_locator)
        ActionChains(self.driver).scroll_to_element(scroll_element).perform()
        self.attach_screenshot()

    @allure.step("Getting window hash for switching")
    def get_window_id(self, index_page):
        return self.driver.window_handles[index_page]

    @allure.step("Switching the browser window")
    def switch_current_window(self, window_id):
        self.driver.switch_to.window(window_id)
