import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.LoanApplication import submit_application
from common import build_subloanapplication_data,build_subloanapplication_jsonschema

@allure.epic("借款申请")
@allure.story("提交借款申请")
@allure.title("提交测试")
@pytest.mark.parametrize("user_data",build_subloanapplication_data())
def Testsubmitloanapplication(user_data):
    res = submit_application(user_data.get("username"),user_data.get("password"),user_data.get("params"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_subloanapplication_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")