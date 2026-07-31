import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Certification import user_info
from common.build_user import build_user_data,build_user_jsonschema

@allure.epic("用户认证")
@allure.story("查询用户信息")
@allure.title("查询信息")
@pytest.mark.parametrize("user_data",build_user_data())
def Testuserinfo(user_data):
    res = user_info(user_data.get("username"),user_data.get("password"),user_data.get("is_online"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_user_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")