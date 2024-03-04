import pytest
from selene import browser
from livelib_project.utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from settings import config, BASE_URL


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
        command_executor=f"https://{config.selenoid_login}:{config.selenoid_pass}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser.config.driver = driver
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
