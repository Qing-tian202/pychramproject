import time
from datetime import datetime
import logging

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from logging.handlers import RotatingFileHandler

from tools import BASE_PATH


class BasePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.__logger = self.get_logger()

    @staticmethod
    def get_logger():
        logger = logging.getLogger('POLogger')
        logger.setLevel(logging.INFO)

        rfh = RotatingFileHandler(filename=BASE_PATH / 'logs/appium_test.log', mode='a', maxBytes=10 * 1024 * 1024,
                                  backupCount=5, encoding='utf-8')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        rfh.setFormatter(formatter)

        logger.addHandler(rfh)

        return logger

    def find_element(self, locator):
        """
        根据locator定位元素
        :param locator: 定位器
        :return: WebElement, 未定位到返回None
        """
        try:
            element = self.wait.until(
                lambda x: x.find_element(*locator)
            )

            return element
        except TimeoutException:
            self.__logger.error(f"Timed out waiting for element to load. locator: {locator}")
            self.take_screenshot()
        except NoSuchElementException:
            self.__logger.error("Element not found! locator: {locator}")
        except Exception as e:
            self.__logger.error(e)

    def click(self, locator):
        """
        点击元素
        :param locator: 定位器
        :return:
        """
        try:
            self.find_element(locator).click()
        except Exception as e:
            self.__logger.error(f"{e}")

    def send_keys(self, keys, locator):
        """
        向元素发送keys
        :param keys: 文本
        :param locator: 定位器
        :return:
        """
        try:
            self.click(locator)
            self.find_element(locator).send_keys(keys)
            self.driver.press_keycode(66)
        except Exception as e:
            self.__logger.error(f"error: {e}")

    def clear_text(self, locator):
        """
        清除文本信息
        :param locator: 定位器
        :return:
        """
        try:
            self.find_element(locator).clear()
        except Exception as e:
            self.__logger.error(e)

    def take_screenshot(self):
        """
        截图
        """
        datestr = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        try:
            s = self.driver.get_screenshot_as_file(BASE_PATH / rf"images/screenshot/{datestr}.png")

            if s:
                self.__logger.info('截图成功')
            else:
                self.__logger.error("截图失败")
        except Exception as e:
            self.__logger.error(e)

    def press_keycode_back(self):
        """点击返回键"""
        self.driver.press_keycode(4)

    def word_by_word_send_keys(self, locator, keys, wait_time=1):
        """
        逐字输入
        :param wait_time: 填字间隔
        :param locator: 定位器
        :param keys: 文本
        :return:
        """
        actions = ActionChains(self.driver)
        element = self.find_element(locator)
        element.click()
        for key in keys:
            actions.send_keys(key)
            actions.pause(wait_time)
        actions.perform()

    def get_text(self, locator):
        """
        获取属性文本信息
        :param locator:
        :return:
        """
        return self.find_element(locator).text

    def get_toast_text(self, expected_text=None):
        """
        获取 Toast 文本

        :param expected_text: 期望包含的文本内容，None 则抓任意 Toast
        :return: Toast 文本字符串，未捕获到返回 None
        """
        locator = ()
        if expected_text:
            xpath = f"//*[contains(@text, '{expected_text}')]"
            locator = (AppiumBy.XPATH, xpath)
        else:
            xpath = "//android.widget.Toast"
            locator = (AppiumBy.XPATH, xpath)

        toast = self.find_element(locator)
        if toast:
            return toast.text
        else:
            return

    def shell(self, command, args=list[str] | str, timeout=5000, include_stderr=True):
        """
        简化版 mobile:shell 调用
        :param command: shell 命令，如 'pm', 'am', 'input'
        :param args: list[str]，如 ['list', 'packages'];或者 "pm list packages"
        :param timeout: 毫秒
        :param include_stderr: 是否返回 stderr
        """
        payload = {
            "command": command,
            "includeStderr": include_stderr,
            "timeout": timeout,
        }
        print(type(args))
        if type(args) is list:
            payload["args"] = args
        elif type(args) is str:
            payload["args"] = args.split()
        else:
            raise TypeError('args参数类型异常')

        return self.driver.execute_script("mobile: shell", payload)
