from livelib_project.pages.web.authorisation import AuthPage
from settings import config
import  allure

@allure.label("owner", "didarphin")
@allure.feature("Check success login")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.BLOCKER)
@allure.label('layer', 'web')
def test_success_auth():
    page = AuthPage()
    page.open_main_page()

    page.open_auth()
    page.enter_login(config.login)
    page.enter_password(config.password)
    page.check_success_auth()

@allure.label("owner", "didarphin")
@allure.feature("Check login with incorrect password")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
def test_incorrect_password():
    page = AuthPage()
    page.open_main_page()

    page.open_auth()
    page.enter_login(config.login)
    page.enter_password("123")
    page.check_incorrect_pass_label()

@allure.label("owner", "didarphin")
@allure.feature("Check login with incorrect login")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
def test_incorrect_login():
    page = AuthPage()
    page.open_main_page()

    page.open_auth()
    page.enter_login("config.login")
    page.check_incorrect_login_label()