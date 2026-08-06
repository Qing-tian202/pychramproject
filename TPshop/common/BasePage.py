import os
import sys
from typing import Union, Tuple

import datetime

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import time
from datetime import datetime
from tools import setup_logging,BASE_DIR
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: Union[webdriver.Chrome, webdriver.Firefox]):
        self.__driver = driver
        self.logger = setup_logging()
        self.wait = WebDriverWait(driver, 20, 0.5)

    @property
    def driver(self):
        return self.__driver

    def find_element(self, locator: Tuple[str, str]):
        try:
            ele = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"定位成功：{ele}, 定位器:{locator}")
            return ele
        except Exception as e:
            self.logger.critical(f"元素定位失败！定位器: {locator}。报错：{e}")

    def send_keys(self, locator: Tuple[str, str], value: str):
        try:
            ele = self.find_element(locator)
            ele.send_keys(value)
        except Exception as e:
            self.logger.critical(f"向元素发送文本失败！定位器是: {locator}。报错：{e}")
            self.take_screenshot()

    def click(self, locator: Tuple[str, str]):
        try:
            ele = self.find_element(locator)
            ele.click()
        except Exception as e:
            self.logger.critical(f"点击元素失败！定位器: {locator}。报错：{e}")
            self.take_screenshot()

    def clear(self, locator: Tuple[str, str]):
        try:
            ele = self.find_element(locator)
            ele.clear()
        except Exception as e:
            self.logger.critical(f"点击元素失败！定位器: {locator}。报错：{e}")
            self.take_screenshot()

    def get_text(self, locator: Tuple[str, str]):
        try:
            ele = self.find_element(locator)
            return ele.text
        except Exception as e:
            self.logger.critical(f"点击元素失败！定位器: {locator}。报错：{e}")
            self.take_screenshot()


    def take_screenshot(self):
        try:
            cur_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

            result = self.__driver.get_screenshot_as_file(BASE_DIR / f'logs/screenshot/{cur_time}.png')
            if result:
                self.logger.info(f"截图成功！图片名: {cur_time}.png")
            else:
                self.logger.error(f"截图失败！图片名: {cur_time}.png")
        except Exception as e:
            self.logger.error(f"未知错误： {e}")