from selene import browser, have
from settings import BASE_URL
import allure


class MessagePage:
    @allure.step("Open main auth_page")
    def open_main_page(self):
        browser.open(BASE_URL)
        return self

    @allure.step("Open outcoming messages")
    def open_outcoming_messages(self):
        browser.open(BASE_URL + "/messages/out")
        return self

    @allure.step("Open new message auth_page")
    def open_new_message_page(self):
        browser.open(BASE_URL + "/message/send")
        return self

    @allure.step("Open incoming messages")
    def open_incoming_messages(self):
        browser.open(BASE_URL + "/messages/in")
        return self

    @allure.step("Agree cookies")
    def agree_cookies(self):
        browser.element(".btn-cookies-agree").double_click()

    @allure.step("Find recepient for new message")
    def find_recipient(self, recepient_login):
        browser.element(".ll-user-search").click().type(recepient_login)
        browser.element("#search-res-users-hint-1").click()

    @allure.step("Type message text")
    def type_message(self, message_text):
        browser.element(".ed_textarea ").type(message_text)

    @allure.step("Send new message")
    def send_message(self):
        browser.element(".ll-submit-btn").click()

    @allure.step("Find sender")
    def find_sender(self):
        browser.all(".mrow-login")[0].should(have.text("Штафенгауэр Карина"))

    @allure.step("Find message text")
    def find_message_text(self, message):
        browser.all(".total-text")[0].should(have.text(message))
