import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Investmentoperation import get_investments_summary
from common import build_investmentsummary_data,build_investmentsummary_jsonschema

@allure.epic("投资操作")
@allure.story("统计投资信息")
@allure.title("统计测试")
@pytest.mark.parametrize("user_data",build_investmentsummary_data())
def Testinvestmentsummary(user_data):
    res = get_investments_summary(user_data.get("username"),user_data.get("password"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_investmentsummary_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")