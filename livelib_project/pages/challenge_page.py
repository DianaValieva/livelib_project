from selene import browser, have
from settings import BASE_URL
import allure


class ChallengePage:
    @allure.step("Open main auth_page")
    def open_main_page(self):
        browser.open(BASE_URL)
        return self

    @allure.step("Open challenge page")
    def open_challenge_page(self):
        browser.open(BASE_URL + "/challenge/2024/reader/Didarphin")
        return self

    @allure.step("Click edit button")
    def click_edit_btn(self):
        browser.element(".kv-settings__link ").click()

    @allure.step("Enter new amount for challenge")
    def enter_amount(self, amount):
        browser.element("#amount").double_click().set_value(amount)

    @allure.step("Click save button")
    def save_amount(self):
        browser.element("[type=submit]").click()

    @allure.step("Check new amount for challenge")
    def check_amount(self, amount):
        browser.element(".kv-progress-bar__percentage").should(have.text(str(amount)))
