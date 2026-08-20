import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru_RU")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Remote(command_executor="http://31.130.148.204:4444", options=options)
    yield driver
    if driver:
        driver.quit()