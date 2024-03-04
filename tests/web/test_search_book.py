from livelib_project.pages.search_page import SearchPage
import allure

search_page = SearchPage()


@allure.label("owner", "didarphin")
@allure.feature("Check search book")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_success_search():
    search_page.open_main_page()

    search_page.find_book("Маленький принц")
    search_page.check_book()


@allure.label("owner", "didarphin")
@allure.feature("Check unsuccess search of book")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.MINOR)
@allure.label('layer', 'web')
@allure.tag("web")
def test_unsuccess_search():
    search_page.open_main_page()

    search_page.find_book("mmmmmmmml")
    search_page.check_book_not_found()
