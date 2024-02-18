from src.api.request import send_post_request
from src.api.schemas import login_schema
from jsonschema import validate
from src.common.settings import USER_ID, config


def test_successfull_login():
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

    assert response.status_code == 200
    validate(response.json(), schema=login_schema)
    assert response.json()["object"]["user_id"] == USER_ID


def test_unsuccessfull_login():
    url = "/account/login"
    data_for_login = "user%5Bredirect%5D=&" \
                     "user%5Bonclick%5D=&" \
                     "source=&popup=regform&" \
                     "current_url=https%3A%2F%2Fwww.livelib.ru%2F&" \
                     "is_new_design=ll2019&" \
                     f"user%5Blogin%5D={config.login}&" \
                     "user%5Bpassword%5D=123" \
                     "&rebuild_menu=false"
    header = {"x-requested-with": "XMLHttpRequest"}

    response = send_post_request(url, data=data_for_login, headers=header)

    assert response.status_code == 200
    assert response.json()["message"]   == "Пользователь с указанными логином и паролем не найден"
