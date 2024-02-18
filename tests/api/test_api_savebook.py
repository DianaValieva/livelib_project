import pytest

from src.api.request import send_post_request
from src.api.schemas import save_book_schema
from jsonschema import validate
from src.common.settings import config
import allure

@allure.label("owner", "didarphin")
@allure.feature("Check save book")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'api')
def test_savebook():
    login_url = "/account/login"
    data_for_login = "user%5Bredirect%5D=&" \
                     "user%5Bonclick%5D=&" \
                     "source=&popup=regform&" \
                     "current_url=https%3A%2F%2Fwww.livelib.ru%2F&" \
                     "is_new_design=ll2019&" \
                     f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}" \
                     "&rebuild_menu=false"
    header = {"x-requested-with": "XMLHttpRequest"}

    login_response = send_post_request(login_url, data=data_for_login, headers=header)
    cookies = login_response.cookies

    assert login_response.status_code == 200

    url = "/user/savebook"
    book_id = 43107604
    book_data = "edition_id=1008560137&" \
                "viewmode=btn-add-plus&" \
                "rating=6&" \
                "status=1&" \
                "own=&" \
                "day=0&" \
                "month=2&" \
                "year=2024&" \
                "priority=1&" \
                "selections=&" \
                "tags=&" \
                "work-edition-id=0&" \
                f"userbook_id={book_id}&" \
                "notes=&" \
                "quick=true&" \
                "is_new_design=ll2019&" \
                "forecast=0"

    response = send_post_request(url, data=book_data, headers=header, cookies=cookies)

    assert response.status_code == 200
    validate(response.json(), schema=save_book_schema)
    assert response.json()["ub_id"] == book_id
    assert response.json()["text"] == "Прочитала"

@allure.label("owner", "didarphin")
@allure.feature("Check change status for a book")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'api')
@pytest.mark.parametrize("status_code, status", [(0, "Хочу прочитать"), (1, "Прочитала"), (3, "Не дочитала")])
def test_change_status_for_book(status_code, status):
    login_url = "/account/login"
    data_for_login = "user%5Bredirect%5D=&" \
                     "user%5Bonclick%5D=&" \
                     "source=&popup=regform&" \
                     "current_url=https%3A%2F%2Fwww.livelib.ru%2F&" \
                     "is_new_design=ll2019&" \
                     f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}" \
                     "&rebuild_menu=false"
    header = {"x-requested-with": "XMLHttpRequest"}

    login_response = send_post_request(login_url, data=data_for_login, headers=header)
    cookies = login_response.cookies

    assert login_response.status_code == 200

    url = "/user/savebook"
    book_id = 43107604
    book_data = "edition_id=1008560137&" \
                "viewmode=btn-add-plus&" \
                "rating=6&" \
                f"status={status_code}&" \
                "own=&" \
                "day=0&" \
                "month=2&" \
                "year=2024&" \
                "priority=1&" \
                "selections=&" \
                "tags=&" \
                "work-edition-id=0&" \
                f"userbook_id={book_id}&" \
                "notes=&" \
                "quick=true&" \
                "is_new_design=ll2019&" \
                "forecast=0"

    response = send_post_request(url, data=book_data, headers=header, cookies=cookies)

    assert response.status_code == 200
    validate(response.json(), schema=save_book_schema)
    assert response.json()["ub_id"] == book_id
    assert response.json()["text"] == status
