import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.Information import get_profile
from common.build_profile_data import build_profile_data
from common.build_profile_jsonschema import build_profile_jsonschema


@allure.story("获取用户资料")
@allure.title("获取用户资料")
@pytest.mark.parametrize("profile_data",build_profile_data())
def Testprofileinfo(profile_data):
    with allure.step("获取接口"):
        res = get_profile(profile_data.get("username"),profile_data.get("password"),profile_data.get("is_online"))

    with allure.step("响应状态码断言"):
        assert res.status_code == profile_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_profile_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == profile_data.get("message")