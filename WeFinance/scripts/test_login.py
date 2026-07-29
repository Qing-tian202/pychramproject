import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Certification import login
from common.build_login import build_login_data,build_login_jsonschema

@allure.epic("用户认证")
@allure.story("登录认证")
@allure.title("登录测试")
@pytest.mark.parametrize("login_data",build_login_data())
def Testlogin(login_data):
    res = login(login_data.get("username"),login_data.get("password"),login_data.get("remember_me"))

    with allure.step("响应状态码断言"):
        assert res.status_code == login_data.get("status")

    if res.status_code == login_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_login_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == login_data.get("message")