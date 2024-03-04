import pytest

from livelib_project.utils.request import send_post_request
from livelib_project.schemas.schemas import save_book_schema
from jsonschema import validate
from settings import config
import allure

status_mapping = {
    "Want to read": "Книга добавлена в коллекцию со статусом \"Хочу прочитать\"",
    "Read": "Книга добавлена в коллекцию со статусом \"Прочитала\"",
    "Did not finish reading": "Книга добавлена в коллекцию со статусом \"Не дочитала\""
}


@allure.label("owner", "didarphin")
@allure.feature("Check change status for a book")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'api')
@allure.tag("api")
@pytest.mark.parametrize("status_code, status", [(0, "Want to read"), (1, "Read"), (3, "Did not finish reading")])
def test_change_status_for_book(status_code, status):
    login_url = "/account/login"
    data_for_login = f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}"
    header = {"x-requested-with": "XMLHttpRequest"}

    login_response = send_post_request(login_url, data=data_for_login, headers=header)
    cookies = login_response.cookies

    assert login_response.status_code == 200

    url = "/user/bookstatussave"
    book_id = 43266070
    book_data = "edition_id=1008506461" \
                f"&userbook_id={book_id}" \
                f"&status={status_code}" \
                "&is_new_design=ll2019"

    response = send_post_request(url, data=book_data, headers=header, cookies=cookies)

    assert response.status_code == 200
    s = response.json()
    validate(response.json(), schema=save_book_schema)
    assert response.json()["userbook_id"] == book_id
    assert response.json()["text"] == status_mapping[status]
