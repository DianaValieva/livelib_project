from settings import BASE_URL
from selene import browser, have
import allure


class AuthPage:
    @allure.step("Open main auth_page")
    def open_main_page(self):
        browser.open(BASE_URL)
        return self

    @allure.step("Open auth form")
    def open_auth(self):
        browser.element(".auth_page-header__login").click()

    @allure.step("Enter login")
    def enter_login(self, login):
        browser.element("#checkin-email").type(login)
        browser.all(".reg-popup__btnNext")[0].press_enter()

    @allure.step("Enter password")
    def enter_password(self, password):
        browser.element("[type=Password]").click().type(password)
        browser.all(".reg-popup__btnNext")[1].click()

    @allure.step("Check success login")
    def check_success_auth(self):
        browser.element(".user-nav__toggle").click()
        browser.element(".user-nav__login").should(have.text("Didarphin"))

    @allure.step("Check unsuccess login")
    def check_incorrect_pass_label(self):
        browser.element("#reg-popup__unvalid").should(have.
                                                      text("Пользователь с указанными логином и паролем не найден"))

    @allure.step("Check unsuccess logi n")
    def check_incorrect_login_label(self):
        browser.element("#check-email-nicname-popup__unvalid").should(
            have.text("Никнейм не найден!"))
