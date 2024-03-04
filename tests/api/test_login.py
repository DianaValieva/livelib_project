from livelib_project.utils.request import send_post_request
from livelib_project.schemas.schemas import login_schema, unsucessful_login_schema
from jsonschema import validate
from settings import USER_ID, config
import allure


@allure.label("owner", "didarphin")
@allure.feature("Check successfull login")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.BLOCKER)
@allure.label('layer', 'api')
@allure.tag("api")
def test_successfull_login():
    url = "/account/login"
    data_for_login = f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}"
    header = {"x-requested-with": "XMLHttpRequest"}

    response = send_post_request(url, data=data_for_login, headers=header)

    assert response.status_code == 200
    validate(response.json(), schema=login_schema)
    assert response.json()["object"]["user_id"] == USER_ID


@allure.label("owner", "didarphin")
@allure.feature("Check unsuccessfull login")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'api')
@allure.tag("api")
def test_unsuccessfull_login():
    url = "/account/login"
    data_for_login = f"user%5Blogin%5D={config.login}&" \
                     "user%5Bpassword%5D=123"
    header = {"x-requested-with": "XMLHttpRequest"}

    response = send_post_request(url, data=data_for_login, headers=header)

    assert response.status_code == 200
    validate(response.json(), schema=unsucessful_login_schema)
    assert response.json()["message"] == "Пользователь с указанными логином и паролем не найден"
