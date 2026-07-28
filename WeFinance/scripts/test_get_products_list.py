import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.BorrowProducts import get_borrow_products_list
from common import build_productslist_data,build_productslist_jsonschema

@allure.epic("借款产品")
@allure.story("获取产品列表")
@allure.title("获取测试")
@pytest.mark.parametrize("user_data",build_productslist_data())
def Testproductslist(user_data):
    res = get_borrow_products_list(user_data.get("params"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_productslist_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")