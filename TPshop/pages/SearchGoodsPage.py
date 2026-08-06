import os
import sys
from typing import Union

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import TP_HOST
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages import LoginPage

class SearchGoodsPage(LoginPage):
    def __init__(self, driver: Union[webdriver.Chrome, webdriver.Firefox]) -> None:
        super().__init__(driver)

        self.__url = TP_HOST + "/Home/Index/index.html"
        self.__goods_description_locator = (By.ID, "q")
        self.__search_btn_locator = (By.CLASS_NAME, "ecsc-search-button")
        self.__search_success_locator = (By.XPATH, "//div[contains(@class, 'shop_name2')]//a")
        self.__search_failure_locator = (By.CLASS_NAME, "ncyekjl")
        self.__search_goods_number_locator = (By.CLASS_NAME, "all-sec")

    def open_search_page(self):
        self.driver.get(self.__url)

    def enter_goods_description(self, value):
        self.send_keys(self.__goods_description_locator, value)

    def click_search_btn(self):
        self.click(self.__search_btn_locator)

    def get_search_success(self):
        return self.get_text(self.__search_success_locator)

    def get_search_failure(self):
        return self.get_text(self.__search_failure_locator)

    def get_search_goods_number(self):
        return self.get_text(self.__search_goods_number_locator)