
from selene import browser, by, have
from settings import BASE_URL

class SearchPage:
    def open_main_page(self):
        browser.open(BASE_URL)
        return self
    def open_outcoming_messages(self):
        browser.open(BASE_URL+"/message/out")
        return self

    def find_book(self, book_name):
        browser.element(".ll-input-search").type(book_name)

    def check_book(self):
        browser.element(".book-item__author").should(have.text("Антуан де Сент-Экзюпери"))

    def check_book_not_found(self):
        browser.element(".suggestion-block").should(have.text("ничего не найдено"))