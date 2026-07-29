import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Certification import logout
from common.build_logout import build_logout_data,build_logout_jsonschema

@allure.epic("用户认证")
@allure.story("用户退出")
@allure.title("登录退出")
@pytest.mark.parametrize("logout_data",build_logout_data())
def Testlogout(logout_data):
    res = logout(logout_data.get("username"),logout_data.get("password"))

    with allure.step("响应状态码断言"):
        assert res.status_code == logout_data.get("status")

    if res.status_code == logout_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_logout_jsonschema())
