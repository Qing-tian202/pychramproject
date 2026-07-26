import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.ApplicationInterface import signup
from common.build_signup_data import build_signup_data
from common.build_signup_jsonschema import build_signup_jsonschema


@allure.story("用户注册")
@allure.title("注册检测")
@pytest.mark.parametrize("signup_data",build_signup_data())
def Testsignup(signup_data):
    with allure.step("注册接口"):
        res = signup(signup_data.get("username"),
                     signup_data.get("email"),
                     signup_data.get("phone"),
                     signup_data.get("password1"),
                     signup_data.get("password2"),)

    with allure.step("响应状态码断言"):
        assert res.status_code == signup_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_signup_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == signup_data.get("message")

        with allure.step("errors断言"):
            assert res.json().get("errors") == signup_data.get("errors")