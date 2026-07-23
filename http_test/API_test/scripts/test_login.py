import pytest
import allure
from case import login
from common import build_login_data


@allure.story("用户认证")
@allure.title("登录认证")
@pytest.mark.parametrize("login_data",build_login_data())
def Testlogin(login_data):
    res = login(login_data.get("username"),login_data.get("password"),login_data.get("authCode"))
    assert res.status_code == login_data.get("status_code")

    if res.status_code >= 400:
        assert res.errcode == login_data.get("errCode")
        assert res.errmsg == login_data.get("errMsg")


