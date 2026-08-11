import time

import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options

from tools import BASE_PATH, APPIUM_SERVER


class DriverFactory(object):
    def __init__(self, yaml_path="config/caps.yml"):
        self.yaml_path = yaml_path

        self.__config: dict = self.load_caps()

    def load_caps(self) -> dict:
        """加载APP基础能力配置文件"""
        with open(BASE_PATH / self.yaml_path, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

            return yaml_data

    def get_driver(
            self,
            device_key: str = "emulator_9",
            app_key: str = "netease_news",
    ) -> webdriver.Remote:
        """
        按需组合：设备 + App + 公共配置
        """
        device_caps = self.__config["devices"].get(device_key, {})
        app_caps = self.__config["android_apps"].get(app_key, {})
        common_caps = self.__config["common"]

        caps_dict = {**device_caps, **app_caps, **common_caps}
        options = UiAutomator2Options()
        # print(caps_dict)
        options.load_capabilities(caps_dict)

        driver = webdriver.Remote(command_executor=APPIUM_SERVER, options=options)

        return driver


if __name__ == '__main__':
    df = DriverFactory()
    df.get_driver()
