from selene import browser, by, have
from settings import BASE_URL
import allure


class SearchPage:
    @allure.step("Open main auth_page")
    def open_main_page(self):
        browser.open(BASE_URL)
        return self

    @allure.step("Type book name in search field")
    def find_book(self, book_name):
        browser.element(".ll-input-search").type(book_name)

    @allure.step("Check book")
    def check_book(self):
        browser.element(".book-item__author").should(have.text("Антуан де Сент-Экзюпери"))

    @allure.step("Check that book not found")
    def check_book_not_found(self):
        browser.element(".suggestion-block").should(have.text("ничего не найдено"))
