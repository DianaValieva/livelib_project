import logging
import allure
from requests import Response
from allure_commons.types import AttachmentType
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response: Response):
    logger.info(f"REQUEST METHOD: {response.request.method}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.request.headers}")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {response.text}\n.\n.")


def attach(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
