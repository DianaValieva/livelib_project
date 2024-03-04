from livelib_project.pages.message_page import MessagePage
from livelib_project.utils.request import authorise_and_get_cookies
import allure
from selene import browser

message_page = MessagePage()


@allure.label("owner", "didarphin")
@allure.feature("Check sending message")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_send_message():
    message_page.open_main_page()
    authorise_and_get_cookies(browser)

    message_page.open_new_message_page()
    message_page.agree_cookies()
    message_page.find_recipient("di7051")

    message_page.type_message("Римская империя — постреспубликанский период Древнего Рима!")
    message_page.send_message()
    message_page.open_outcoming_messages()
    message_page.find_message_text("Римская империя")


@allure.label("owner", "didarphin")
@allure.feature("Check incoming message")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_find_incoming_message():
    message_page.open_main_page()

    authorise_and_get_cookies(browser)

    message_page.open_incoming_messages()
    message_page.agree_cookies()

    message_page.find_sender()
    message_page.find_message_text("Привет")
