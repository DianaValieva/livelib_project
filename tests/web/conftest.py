import pytest
from selene import browser


@pytest.fixture(scope="function",autouse=True)
def set_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.driver.maximize_window()
    yield browser
    browser.quit()