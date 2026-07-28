import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
import jsonschema
from case.RealNameVerification import change_photo
from common import build_changephoto_data,build_changephoto_jsonschema

@allure.epic("实名认证")
@allure.story("修改用户头像")
@allure.title("修改测试")
@pytest.mark.parametrize("user_data",build_changephoto_data())
def Testaddcard(user_data):
    res = change_photo(user_data.get("username"),user_data.get("password"),user_data.get("avatar_path"),user_data.get("image_type"))

    with allure.step("响应状态码断言"):
        assert res.status_code == user_data.get("status")

    if res.status_code == 200:
        with allure.step("jsonschema断言"):
            jsonschema.validate(res.json(),build_changephoto_jsonschema())

    if res.status_code >= 400:
        with allure.step("message断言"):
            assert res.json().get("message") == user_data.get("message")