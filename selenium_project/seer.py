import time
import random
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



class Seer(BaseAppium):
    def __init__(self, driver: webdriver.Remote):
        super().__init__(driver)

        self.__seer_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR,
                                    'new UiSelector().text("赛尔号巅峰之战")')
        self.__search_txt_locator = [(71,375)]
        self.__search_1_locator = [(130,850)]
        self.__search_config_locator = [(1270,350)]
        self.__chose_music_locator = [(646,748)]
        self.__fight_locator = [(random.randint(135,165),random.randint(661,701))]
        self.__skill_locator = [(random.randint(378,410),random.randint(786,820))]
        self.__finish_locator = [(random.randint(1130,1170),random.randint(760,800))]

    @staticmethod
    def set_driver():
        options = UiAutomator2Options()
        options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "15.0",
        "appium:deviceName": "emulator-55556",
        "appium:appPackage": "app.lawnchair",
        "appium:appActivity": "app.lawnchair.LawnchairLauncher",
        "appium:appWaitActivity": "*",
        "appium:automationName": "UiAutomator2",
        "appium:no_reset": True,
        "appium:dontStopAppOnReset": True
        })

        driver = webdriver.Remote('http://localhost:4723', options=options)

        return driver

    def close(self):
        self.driver.quit()

    def set_up(self):
        self.click(self.__seer_btn_locator)
        print("点击应用")
        time.sleep(30)
        self.driver.tap(self.__search_config_locator)
        print("点击登录")
        time.sleep(30)
        self.driver.tap(self.__search_txt_locator)
        print("点击获取")
        time.sleep(10)
        self.driver.tap(self.__search_1_locator)
        print("点击收藏")
        time.sleep(10)
        self.driver.tap(self.__search_config_locator)
        print("点击前往")
        time.sleep(10)
        self.driver.tap(self.__chose_music_locator)
        print("点击第四关")
        time.sleep(10)

    def run(self):
        self.driver.tap(self.__fight_locator)
        time.sleep(5)
        self.driver.tap(self.__skill_locator)
        time.sleep(5)
        self.driver.tap(self.__finish_locator)
        time.sleep(5)


if __name__ == '__main__':
    setting = Seer(Seer.set_driver())
    setting.set_up()
    while True:
        setting.run()
        # times = 20
        # while times:
        #     setting.run()
        #     times -= 1
        # op = int(input("是否继续1 继续，0 退出 :"))
        # if op == 0:
        #     break