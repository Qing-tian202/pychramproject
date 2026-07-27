import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Information import update_profile
from common.build_update_data import build_update_data
from common.build_update_jsonschema import build_update_jsonschema


@allure.story("更新用户资料")
@allure.title("更新用户资料")
@pytest.mark.parametrize("update_data",build_update_data())
def Testupdateinfo(update_data):
    with allure.step("更新接口"):
        res = update_profile(update_data.get("username"),update_data.get("password"),update_data.get("is_online"),update_data.get("data"))

    with allure.step("响应状态码断言"):
        assert res.status_code == update_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_update_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == update_data.get("message")