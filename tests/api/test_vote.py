import pytest

from livelib_project.utils.request import send_post_request
from livelib_project.schemas.schemas import vote_schema
from jsonschema import validate
from settings import config
import allure


@allure.label("owner", "didarphin")
@allure.feature("Check vote for diffetent objects")
@allure.label('microservice', 'API')
@allure.severity(severity_level=allure.severity_level.CRITICAL)
@allure.label('layer', 'api')
@allure.tag("api")
@pytest.mark.parametrize("vote, object_id, object_type", [(0, 4029199, "review"), (1, 14443822, "comment")])
def test_vote(vote, object_id, object_type):
    login_url = "/account/login"
    data_for_login = f"user%5Blogin%5D={config.login}&" \
                     f"user%5Bpassword%5D={config.password}"
    header = {"x-requested-with": "XMLHttpRequest"}

    login_response = send_post_request(login_url, data=data_for_login, headers=header)
    cookies = login_response.cookies

    assert login_response.status_code == 200
    url = "/vote"
    vote_data = f"id={object_id}" \
                f"&vote={vote}" \
                f"&alias={object_type}"

    response = send_post_request(url, data=vote_data, headers=header, cookies=cookies)

    assert response.status_code == 200
    validate(response.json(), schema=vote_schema)
    assert response.json()["object_id"] == object_id
    assert response.json()["object_alias"] == object_type
