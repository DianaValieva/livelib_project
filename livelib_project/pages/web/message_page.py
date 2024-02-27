from selene import browser, by, have
from settings import BASE_URL

class MessagePage:
    def open_main_page(self):
        browser.open(BASE_URL)
        return self
    def open_outcoming_messages(self):
        browser.open(BASE_URL+"/messages/out")
        return self

    def open_new_message_page(self):
        browser.open(BASE_URL+"/message/send")
        return self

    def open_incoming_messages(self):
        browser.open(BASE_URL+"/messages/in")
        return self

    def close_ads(self):
        browser.element(".btn-close").click()

    def agree_cookies(self):
        browser.element(".btn-cookies-agree").double_click()
    def find_recipient(self, recepient_login):
        browser.element(".ll-user-search").click().type(recepient_login)
        browser.element("#search-res-users-hint-1").click()

    def type_message(self, message_text):
        browser.element(".ed_textarea ").type(message_text)

    def send_message(self):
        browser.element(".ll-submit-btn").click()

    def find_sender(self):
        browser.all(".mrow-login")[0].should(have.text("Штафенгауэр Карина"))


    def find_message_text(self, message):
        b=browser.all(".total-text")[0].locate()
        browser.all(".total-text")[0].should(have.text(message))

    def find_first_message(self):
        b=browser.all("")[0].locate().get_attribute("data-message_id")
        ...


