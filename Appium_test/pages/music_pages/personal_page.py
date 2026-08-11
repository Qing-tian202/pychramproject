import time

from appium.webdriver.common.appiumby import AppiumBy

from common.base_page import BasePage
from appium import webdriver

class PersonalPage(BasePage):
    def __init__(self, driver:webdriver.Remote):
        super().__init__(driver)

        # 昵称
        self.__nickname_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/nicknameTV")')
        # 个人主页
        self.__center_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/cl_qq_login")')
        # 选择音乐
        self.__music_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(3)')

    def click_music(self):
        self.click(self.__music_locator)

    def click_center(self):
        self.click(self.__center_locator)

    def get_nickname(self):
        return self.get_text(self.__nickname_locator)