import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import time
from tools import setup_logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: webdriver.Chrome|webdriver.Firefox):
        self.__driver = driver
        self.__logger = setup_logging()

    @property
    def driver(self):
        return self.driver

    def locate(self, locator: tuple[str, str]):
        self.__driver.find_element(*locator)

    def send_keys(self,):
        self.__driver.find_element()