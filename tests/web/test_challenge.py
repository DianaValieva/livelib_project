from livelib_project.pages.challenge_page import ChallengePage
from livelib_project.utils.request import authorise_and_get_cookies
import allure
import random

challenge_page = ChallengePage()


@allure.label("owner", "didarphin")
@allure.feature("Check changing challenge amount")
@allure.label('microservice', 'WEB')
@allure.severity(severity_level=allure.severity_level.NORMAL)
@allure.label('layer', 'web')
@allure.tag("web")
def test_change_challenge_amount():
    challenge_page.open_main_page()
    authorise_and_get_cookies()

    challenge_page.open_challenge_page()
    challenge_page.click_edit_btn()
    new_amount = random.randint(1, 100)
    challenge_page.enter_amount(new_amount)
    challenge_page.save_amount()
    challenge_page.check_amount(new_amount)
