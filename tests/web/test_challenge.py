from livelib_project.pages.challenge_page import ChallengePage
from livelib_project.utils.request import authorise_and_get_cookies
import allure
from selene import browser
import random

chalenge_page = ChallengePage()


@allure.label("owner", "didarphin")
@allure.feature("Check changing challenge amount")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_change_challenge_amount():
    chalenge_page.open_main_page()
    authorise_and_get_cookies()

    chalenge_page.open_challenge_page()
    chalenge_page.click_edit_btn()
    new_amount = random.randint(1, 100)
    chalenge_page.enter_amount(new_amount)
    chalenge_page.save_amount()
    chalenge_page.check_amount(new_amount)
