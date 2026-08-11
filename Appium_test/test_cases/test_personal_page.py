import time

import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from common.driver_factory import DriverFactory
from common.build_music_data import build_music_data
from pages.music_pages.personal_page import PersonalPage

@allure.feature("用户认证")
@allure.story("查询昵称")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
@pytest.mark.smoke
class TestPersonalPage:
    def setup_method(self):
        with allure.step("获取驱动"):
            self.driver = DriverFactory().get_driver(device_key="auto_motive",app_key="applist")
        with allure.step("打开应用列表"):
            self.login_page = PersonalPage(self.driver)
            time.sleep(2)
        with allure.step("点击媒体中心"):
            self.login_page.click_music()
            time.sleep(2)
        with allure.step("点击个人主页"):
            self.login_page.click_center()
            time.sleep(2)

    def teardown_method(self):
        with allure.step("退出驱动"):
            self.driver.quit()

    @pytest.mark.parametrize("data", build_music_data())
    def test_personal_page(self, data:dict):
        allure.dynamic.title(data['description'])

        with allure.step("断言"):
            if data['flag'] == 0:

                actual = self.login_page.get_nickname()
                assert data['expect'] in actual
            else:
                actual = self.login_page.get_toast_text()
                assert data['expect'] in actual

