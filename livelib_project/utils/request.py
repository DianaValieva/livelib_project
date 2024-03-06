import requests
import allure
import curlify
from allure_commons.types import AttachmentType
from settings import BASE_URL, config
from livelib_project.utils.logger import log, attach
from selene import browser


def send_post_request(url, **kwargs):
    url = BASE_URL + url
    with allure.step(f"POST {url}"):
        response = requests.post(url, **kwargs)
        curl = curlify.to_curl(response.request)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        log(response)
        attach(response)
        return response


def authorise_and_get_cookies():
    url = "/account/login"
    data_for_login = "user%5Bredirect%5D=&" \
                     "user%5Bonclick%5D=&" \
                     "source=&popup=regform&" \
                     "current_url=https%3A%2F%2Fwww.livelib.ru%2F&" \
                     "is_new_design=ll2019&" \
                     f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}" \
                     "&rebuild_menu=false"
    header = {"x-requested-with": "XMLHttpRequest"}
    response = send_post_request(url, data=data_for_login, headers=header)

    cookies = response.cookies.get_dict()

    for name, cookie in cookies.items():
        browser.driver.add_cookie({'name': name, 'value': cookie})
