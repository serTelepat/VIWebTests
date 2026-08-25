import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru_RU")
    driver = webdriver.Remote(command_executor="http://31.130.148.204:4444", options=options)
    try:
        yield driver
    finally:
        driver.quit()