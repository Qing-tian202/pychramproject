import time

import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from common.driver_factory import DriverFactory
from pages.netease_pages.login_page import LoginPage
from common.build_data import build_login_data


@allure.feature("用户认证")
@allure.story("登录测试")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.smoke
class TestLogin:
    """测试登录成功"""

    def setup_method(self):
        with allure.step("获取驱动"):
            self.driver = DriverFactory().get_driver()
        with allure.step("打开网易新闻"):
            self.login_page = LoginPage(self.driver)
        with allure.step("导航至登陆页面"):
            self.login_page.navigate_to_login_page()

    @pytest.mark.parametrize("data", build_login_data())
    def test_login(self, data):
        allure.dynamic.title(data['description'])

        with allure.step("输入用户名"):
            self.login_page.enter_username(data['username'])
            self.login_page.press_keycode_back()
        with allure.step("输入用户密码"):
            self.login_page.enter_password(data['password'])
        with allure.step("点击登录按钮"):
            self.login_page.click_login_btn()
        time.sleep(2)

        with allure.step("断言"):
            if data['flag'] == 0:
                self.login_page.click((AppiumBy.XPATH, '//*[@text="我"]'))
                time.sleep(2)

                actual = self.login_page.get_nick_name()
                assert data['expect'] in actual
            else:
                actual = self.login_page.get_toast_text()
                assert data['expect'] in actual

    def teardown_method(self):
        with allure.step("退出驱动"):
            self.driver.quit()
