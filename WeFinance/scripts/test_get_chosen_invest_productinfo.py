import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Investmentproduct import get_investment_info
from common import build_investproductid_data,build_investproductid_jsonschema

@allure.epic("投资产品")
@allure.story("获取指定产品")
@allure.title("获取测试")
@pytest.mark.parametrize("user_data",build_investproductid_data())
def Testchoseninvestproductinfo(user_data):
    res = get_investment_info(user_data.get("product_id"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_investproductid_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")