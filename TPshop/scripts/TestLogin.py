import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages import LoginPage
from build_tools import build_login

@allure.feature("登录测试")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
class TestLogin:
    def setup_class(self) -> None:
        executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path = executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--start-maximized')

        driver = webdriver.Chrome(service=service, options=options)

        self.lp = LoginPage(driver)

    def teardown_class(self) -> None:
        self.lp.driver.quit()

    @pytest.mark.parametrize("case", build_login())
    def test_login(self, case:dict) -> None:
        with allure.step("打开页面"):
            self.lp.open_login_page()
            time.sleep(1)
        with allure.step("输入用户名"):
            self.lp.enter_username(case.get("username"))
            time.sleep(1)
        with allure.step("输入用户密码"):
            self.lp.enter_password(case.get("password"))
            time.sleep(1)
        with allure.step("输入验证码"):
            self.lp.enter_verify_code(case.get("code"))
            time.sleep(1)
        with allure.step("登录"):
            self.lp.click_login()
            time.sleep(2)

        if not case.get("flag"):
            allure.dynamic.story("登录成功")
            with allure.step("断言昵称"):
                assert self.lp.get_nick_name() == case.get("expect")
            with allure.step("登录退出"):
                self.lp.click_logout()
        else:
            allure.dynamic.story("登录失败")
            with allure.step("断言错误文本信息"):
                assert self.lp.get_pop_view_text() == case.get("expect")