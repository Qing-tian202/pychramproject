import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Investmentoperation import invest
from common import build_investoperate_data,build_investoperate_jsonschema

@allure.epic("投资操作")
@allure.story("投资指定产品")
@allure.title("投资测试")
@pytest.mark.parametrize("user_data",build_investoperate_data())
def Testinvestoperate(user_data):
    res = invest(user_data.get("username"),user_data.get("password"),user_data.get("params"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == user_data.get("status") and res.status_code < 400:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_investoperate_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")