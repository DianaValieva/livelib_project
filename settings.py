import pydantic
from dotenv import load_dotenv
import os

BASE_URL = "https://www.livelib.ru"
USER_ID = 217350

class Config(pydantic.BaseModel):
    load_dotenv()
    login: str = os.environ.get('USER')
    password: str = os.environ.get('PASSWORD')
    selenoid_login:str = os.environ.get("S_USER")
    selenoid_pass:str = os.environ.get("S_PASSWORD")


config = Config()