import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.RealNameVerification import photo_image
from common import build_getphoto_data,build_getphoto_jsonschema

@allure.epic("实名认证")
@allure.story("获取用户头像")
@allure.title("获取测试")
@pytest.mark.parametrize("user_data",build_getphoto_data())
def Testaddcard(user_data):
    res = photo_image(user_data.get("username"),user_data.get("password"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_getphoto_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")