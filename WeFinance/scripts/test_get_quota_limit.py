import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case import get_quota_limit
from common import build_getquotalimit_data,build_getquotalimit_jsonschema

@allure.epic("还款")
@allure.story("查看借款额度")
@allure.title("查看测试")
@pytest.mark.parametrize("user_data",build_getquotalimit_data())
def Testgetquotalimit(user_data):
    res = get_quota_limit(user_data.get("username"),user_data.get("password"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_getquotalimit_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")