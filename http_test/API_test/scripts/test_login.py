import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
from case.get_login import login
from common.build_login_data import build_login_data


@allure.story("用户认证")
@allure.title("登录认证")
@pytest.mark.parametrize("login_data",build_login_data())
def Testlogin(login_data):
    res = login(login_data.get("username"),login_data.get("password"),login_data.get("authCode"))
    assert res.status_code == login_data.get("status_code")

    if res.status_code >= 400:
        assert res.json().get("errCode") == login_data.get("errCode")
        assert res.json().get("errMsg") == login_data.get("errMsg")


