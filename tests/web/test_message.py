from livelib_project.pages.web.message_page import MessagePage
from livelib_project.utils.request import authorise_and_get_cookies
import allure
from selene import browser

@allure.label("owner", "didarphin")
@allure.feature("Check sending message")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
def test_send_message():
    page = MessagePage()
    page.open_main_page()

    cookies = authorise_and_get_cookies()
    browser.driver.add_cookie({"name": "LiveLibId", "value": cookies["LiveLibId"]}),
    browser.driver.add_cookie({"name": "ll_asid", "value": cookies["ll_asid"]}),
    browser.driver.add_cookie({"name": "llsid", "value": cookies["llsid"]}),

    page.open_new_message_page()
    page.agree_cookies()
    page.find_recipient("di7051")

    page.type_message("Римская империя — постреспубликанский период Древнего Рима!")
    page.send_message()
    page.open_outcoming_messages()
    page.find_message_text("Римская империя")


@allure.label("owner", "didarphin")
@allure.feature("Check incoming message")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
def test_find_incoming_message():
    page = MessagePage()
    page.open_main_page()

    cookies = authorise_and_get_cookies()
    browser.driver.add_cookie({"name": "LiveLibId", "value": cookies["LiveLibId"]}),
    browser.driver.add_cookie({"name": "ll_asid", "value": cookies["ll_asid"]}),
    browser.driver.add_cookie({"name": "llsid", "value": cookies["llsid"]}),

    page.open_incoming_messages()
    page.agree_cookies()

    page.find_sender()
    page.find_message_text("Привет")
