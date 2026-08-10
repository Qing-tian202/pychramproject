import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class App_Operate:
    def __init__(self,driver:webdriver.Remote):
        self.__driver = driver
        self.__login_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().resourceId('tv.danmaku.bili:id/avatar_layout')")
        self.__game_center_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('游戏中心,按钮')")
        self.__message_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('消息,按钮')")
        self.__label_01_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('直播,6之1,标签')")
        self.__label_02_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('推荐,6之2,标签')")
        self.__label_03_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('热门,6之3,标签')")
        self.__label_04_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('动画,6之4,标签')")
        self.__label_05_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('影视,6之5,标签')")
        self.__label_06_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().description('新征程,6之6,标签')")
        self.__partition_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('tv.danmaku.bili:id/category_image')")

    def get_label_01(self):
        pass

