import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def set_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.driver.maximize_window()
    yield browser
    browser.quit()