import time
from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAppium:
    def __init__(self,driver:webdriver.Remote):
        self.__driver = driver
        self.wait = WebDriverWait(driver,10)

    @property
    def driver(self):
        return self.__driver


    def find_element(self,locator:tuple[str,str]):
        try:
            ele = self.wait.until(EC.visibility_of_element_located(locator))
            return ele
        except Exception as e:
            print(f"定位出错：{e}")

    def send_keys(self,locator:tuple[str,str],value):
        ele = self.find_element(locator)
        ele.send_keys(value)

    def click(self,locator:tuple[str,str]):
        ele = self.find_element(locator)
        ele.click()

class Setting(BaseAppium):
    def __init__(self,driver:webdriver.Remote):
        super().__init__(driver)

        self.__music_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(3)')
        self.__search_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/ll_search")')
        self.__search_txt_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/edit_text")')
        self.__search_config_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/confirm_btn")')
        self.__chose_music_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tinnove.mediacenter:id/ll_search_item_bg").instance(2)')




    @staticmethod
    def set_driver():
        options = UiAutomator2Options()
        options.load_capabilities({
          "platformName": "Android",
          "appium:platformVersion": "11",
          "appium:deviceName": "69a96763",
          "appium:appPackage": "com.tinnove.launcher",
          "appium:appActivity": "com.tinnove.applist.AppListActivity",
          "appium:noReset": True,
          "appium:automationName": "UiAutomator2"
        })

        driver = webdriver.Remote('http://localhost:4723', options=options)

        return driver

    def close(self):
        self.driver.quit()


    def run(self):
        self.click(self.__music_btn_locator)
        time.sleep(2)
        self.click(self.__search_btn_locator)
        time.sleep(2)
        self.send_keys(self.__search_txt_locator, "天后")
        time.sleep(2)
        self.click(self.__search_config_locator)
        time.sleep(2)
        self.click(self.__chose_music_locator)
        time.sleep(2)
        self.close()


if __name__ == '__main__':
    setting = Setting(Setting.set_driver())
    setting.run()