import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePageLocators:

    ### ---------- BASIC HELP PAGE ---------- ###
    OK_LOGO_BUTTON_TOOLBAR = (By.XPATH, "//*[@data-l='t,logo']//div")
    SEARCH_INPUT_TOOLBAR = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-search-input']")
    SEARCH_BUTTON_TOOLBAR = (By.XPATH, "//div[@id='topPanel']//*[@data-tsid='toolbar-searchButton']")
    VK_SERVICES_BUTTON = (By.XPATH, "//*[@aria-label='Сервисы VK']")

    ## VK SERVICES
    MORE_BUTTON_VK_SERVICES_MENU = (By.XPATH, "//*[@data-l='t,more']")


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        self.find_element(BasePageLocators.OK_LOGO_BUTTON_TOOLBAR)
        self.find_element(BasePageLocators.SEARCH_INPUT_TOOLBAR)
        self.find_element(BasePageLocators.SEARCH_BUTTON_TOOLBAR)
        self.find_element(BasePageLocators.VK_SERVICES_BUTTON)

        with allure.step("Checking the correcting page load"):
            self.attach_screenshot()


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

    @allure.step("Click the VK Services button")
    def click_vk_services_button(self):
        self.find_element(BasePageLocators.VK_SERVICES_BUTTON).click()

    @allure.step("Click the 'more' button")
    def click_more_button(self):
        self.find_element(BasePageLocators.MORE_BUTTON_VK_SERVICES_MENU).click()

    def get_window_id(self, index):
        return self.driver.window_handles[index]

    def switch_current_window(self, window_id):
        self.driver.switch_to.window(window_id)