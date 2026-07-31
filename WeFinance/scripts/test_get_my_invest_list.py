import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Investmentoperation import get_invest_list
from common import build_myinvestproductslist_data,build_myinvestproductslist_jsonschema

@allure.epic("投资操作")
@allure.story("查询我的投资列表")
@allure.title("查询测试")
@pytest.mark.parametrize("user_data",build_myinvestproductslist_data())
def Testmyinvestlist(user_data):
    res = get_invest_list(user_data.get("username"),user_data.get("password"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_myinvestproductslist_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")