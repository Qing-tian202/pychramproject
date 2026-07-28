import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.BankCardManagement import delete_card
from common import build_deletecard_data,build_deletecard_jsonschema

@allure.epic("银行卡管理")
@allure.story("删除银行卡")
@allure.title("删除测试")
@pytest.mark.parametrize("user_data",build_deletecard_data())
def Testdeletecard(user_data):
    res = delete_card(user_data.get("username"),user_data.get("password"),user_data.get("is_online"),user_data.get("card_id"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_deletecard_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")