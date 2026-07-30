import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case import get_chosen_contract_info
from common import build_getcontractinfo_data,build_getcontractinfo_jsonschema

@allure.epic("合同")
@allure.story("查看合同详情")
@allure.title("查看测试")
@pytest.mark.parametrize("user_data",build_getcontractinfo_data())
def Testgetcontractinfomation(user_data):
    res = get_chosen_contract_info(user_data.get("username"),user_data.get("password"),user_data.get("params"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_getcontractinfo_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")