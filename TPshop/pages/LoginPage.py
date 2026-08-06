import os
import sys
from typing import Union

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools import TP_HOST
from selenium import webdriver
from selenium.webdriver.common.by import By

from common import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: Union[webdriver.Chrome, webdriver.Firefox]):
        super().__init__(driver)

        self.__username_locator = (By.ID, 'username')
        self.__password_locator = (By.ID, 'password')
        self.__verify_code_locator = (By.NAME, "verify_code")
        self.__login_btn_locator = (By.NAME, "sbtbutton")
        self.__logout_btn_locator = (By.CSS_SELECTOR,"a[title='退出']")
        self.__register_btn_locator = (By.CLASS_NAME, 'register_c')
        self.__pop_view_locator = (By.CSS_SELECTOR, '.layui-layer-content.layui-layer-padding')
        self.__nick_name_locator = (By.XPATH, '//a[contains(@class,"userinfo")]')
        self.__url = f"{TP_HOST}/Home/user/login.html"

    def open_login_page(self):
        self.driver.get(self.__url)

    def enter_username(self, value):
        self.send_keys(self.__username_locator, value)

    def enter_password(self, value):
        self.send_keys(self.__password_locator, value)

    def enter_verify_code(self, value):
        self.send_keys(self.__verify_code_locator, value)

    def click_login(self):
        self.click(self.__login_btn_locator)

    def click_logout(self):
        self.click(self.__logout_btn_locator)

    def get_nick_name(self):
        return self.get_text(self.__nick_name_locator)

    def get_pop_view_text(self):
        return self.get_text(self.__pop_view_locator)
