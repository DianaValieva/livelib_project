from settings import BASE_URL,config
from selene import browser, by, have


class AuthPage:
    def open_main_page(self):
        browser.open(BASE_URL)
        return self

    def open_auth(self):
        browser.element(".page-header__login").click()

    def enter_login(self, login):
        browser.element("#checkin-email").type(login)
        browser.all(".reg-popup__btnNext")[0].press_enter()

    def enter_password(self, password):
        browser.element("[type=Password]").click().type(password)
        browser.all(".reg-popup__btnNext")[1].click()

    def check_success_auth(self):
        browser.element(".user-nav__toggle").click()
        browser.element(".user-nav__login").should(have.text("Didarphin"))

    def check_incorrect_pass_label(self):
        browser.element("#reg-popup__unvalid").should(have.
            text("Пользователь с указанными логином и паролем не найден"))

    def check_incorrect_login_label(self):
        browser.element("#check-email-nicname-popup__unvalid").should(
            have.text("Никнейм не найден!"))

