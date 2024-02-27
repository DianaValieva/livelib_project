from livelib_project.pages.web.search_page import SearchPage
import allure
@allure.label("owner", "didarphin")
@allure.feature("Check search book")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'web')
def test_success_search():
    page = SearchPage()
    page.open_main_page()

    page.find_book("Маленький принц")
    page.check_book()

@allure.label("owner", "didarphin")
@allure.feature("Check unsuccess search of book")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.MINOR)
@allure.label('layer', 'web')
def test_unsuccess_search():
    page = SearchPage()
    page.open_main_page()

    page.find_book("mmmmmmmml")
    page.check_book_not_found()