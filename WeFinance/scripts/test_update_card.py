import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.BankCardManagement import update_card
from common import build_updatecard_data,build_updatecard_jsonschema

@allure.epic("银行卡管理")
@allure.story("更新银行卡信息")
@allure.title("更新测试")
@pytest.mark.parametrize("user_data",build_updatecard_data())
def Testupdatecard(user_data):
    res = update_card(user_data.get("username"),user_data.get("password"),user_data.get("is_online"),user_data.get("card_id"),user_data.get("new_card"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_updatecard_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")