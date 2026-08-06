import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages import SearchGoodsPage
from build_tools import build_search

@allure.feature("搜索测试")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.search
class TestSearch:
    def setup_class(self) -> None:
        executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path = executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--start-maximized')

        driver = webdriver.Chrome(service=service, options=options)

        self.lp = SearchGoodsPage(driver)

        # 登录账户
        self.lp.open_login_page()
        time.sleep(1)

        self.lp.enter_username("13800138006")
        time.sleep(1)

        self.lp.enter_password("123456")
        time.sleep(1)

        self.lp.enter_verify_code("crxy")
        time.sleep(1)

        self.lp.click_login()
        time.sleep(2)

    def teardown_class(self) -> None:
        self.lp.driver.quit()

    @pytest.mark.parametrize("case", build_search())
    def test_search(self, case:dict) -> None:

        with allure.step("打开首页"):
            self.lp.open_search_page()
            time.sleep(1)
        with allure.step("输入商品名称"):
            self.lp.enter_goods_description(case.get("goods_name"))
            time.sleep(1)
        with allure.step("点击搜索"):
            self.lp.click_search_btn()
            time.sleep(2)


        if not case.get("flag"):
            allure.dynamic.story("搜索成功")
            with allure.step("搜索商品包含目标商品"):
                txt = self.lp.get_search_success()
                res = case.get("goods_name") in txt

                assert res == case.get("expect")
            # with allure.step("登录退出"):
            #     self.lp.click_logout()
        else:
            allure.dynamic.story("搜索失败")
            with allure.step("断言错误文本信息"):
                assert self.lp.get_search_failure() == case.get("expect")

        with allure.step("断言搜索到的商品数"):
            assert self.lp.get_search_goods_number() == case.get("goods_number")