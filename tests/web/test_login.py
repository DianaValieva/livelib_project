from livelib_project.pages.authorization_page import AuthPage
from settings import config
import allure

auth_page = AuthPage()


@allure.label("owner", "didarphin")
@allure.feature("Check success login")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.BLOCKER)
@allure.label('layer', 'web')
@allure.tag("web")
def test_success_auth():
    auth_page.open_main_page()
    auth_page.open_auth()
    auth_page.enter_login(config.login)
    auth_page.enter_password(config.password)
    auth_page.check_success_auth()


@allure.label("owner", "didarphin")
@allure.feature("Check login with incorrect password")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_incorrect_password():
    auth_page.open_main_page()
    auth_page.open_auth()
    auth_page.enter_login(config.login)
    auth_page.enter_password("123")
    auth_page.check_incorrect_pass_label()


@allure.label("owner", "didarphin")
@allure.feature("Check login with incorrect login")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
def test_incorrect_login():
    auth_page.open_main_page()
    auth_page.open_auth()
    auth_page.enter_login("config.login")
    auth_page.check_incorrect_login_label()
