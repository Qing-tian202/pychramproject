import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.get_login import login
from common.build_login_data import build_login_data
from common.build_jsonschema import build_jsonschema_data


@allure.story("用户认证")
@allure.title("登录认证")
@pytest.mark.parametrize("login_data",build_login_data())
def Testlogin(login_data):
    with allure.step("登录接口"):
        res = login(login_data.get("username"),login_data.get("password"),login_data.get("authCode"))

    with allure.step("响应状态码断言"):
        assert res.status_code == login_data.get("status_code")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_jsonschema_data())

    if res.status_code >= 400:
        with allure.step("errCode断言"):
            assert res.json().get("errCode") == login_data.get("errCode")
        with allure.step("errMsg断言"):
            assert res.json().get("errMsg") == login_data.get("errMsg")


