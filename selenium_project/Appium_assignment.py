import time
import re
from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
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

        self.__search_btn_locator = (AppiumBy.ID, "com.android.settings:id/search_action_bar")
        self.__search_txt_locator = (AppiumBy.ID, "android:id/search_src_text")
        self.__search_res_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(8)')
        self.__code_method_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(10)')
        self.__code_map_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.settings:id/lockPattern")')
        self.__config_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.settings:id/footerRightButton")')
        self.__config_btn2_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.settings:id/redaction_done_button")')
        self.__look_none_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.settings:id/lock_none")')
        self.__look_none_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
        self.__first_page_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.systemui:id/lockPatternView")')
        self.__system_file_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("文件夹：系统应用")')
        self.__setting_btn_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("设置")')


    @staticmethod
    def set_driver():
        options = UiAutomator2Options()
        options.load_capabilities({
            "platformName": "Android",
            "appium:platformVersion": "9.0",
            "appium:deviceName": "emulator-5554",
            "appium:appPackage": "com.android.settings",
            "appium:appActivity": ".Settings",
            "appium:unicodeKeyboard": True,
            "appium:resetKeyboard": True,
            'setFlushTouch': True,
            "appium:automationName": "UiAutomator2"
        })

        driver = webdriver.Remote('http://localhost:4723', options=options)

        return driver

    def close(self):
        self.driver.quit()

    def get_points(self,ele):
        # ele = self.find_element(self.__code_map_locator)
        # 提取所有数字
        numbers = re.findall(r'\d+', ele.get_attribute('bounds'))
        # 转换为 int
        numbers = [int(num) for num in numbers]

        x_gap = (numbers[2] - numbers[0]) // 3
        y_gap = (numbers[3] - numbers[1]) // 3

        center_x = (numbers[2] + numbers[0]) // 2
        center_y = (numbers[3] + numbers[1]) // 2

        points = [(center_x-x_gap,center_y+y_gap),(center_x-x_gap,center_y), (center_x-x_gap,center_y-y_gap),
                  (center_x,center_y),
                  (center_x+x_gap,center_y+y_gap),(center_x+x_gap,center_y), (center_x+x_gap,center_y-y_gap),]

        return points


    def drow_map(self,ele):
        finger = PointerInput(POINTER_TOUCH, "finger")
        actions = ActionBuilder(driver = self.driver, mouse = finger)

        # points = [(680,700),(680,582),(680,461),(800,582),(920,700),(920,582),(927,461)]
        points = self.get_points(ele)

        # 按下并移动
        actions.pointer_action.move_to_location(points[0][0], points[0][1])
        actions.pointer_action.pointer_down()

        for x, y in points[1:]:
            actions.pointer_action.move_to_location(x, y)

        actions.pointer_action.pointer_up()

        # 执行
        actions.perform()

    def click_power(self):
        # 统一入口：driver.execute_script("mobile: shell", <args_map>)
        self.driver.execute_script("mobile: shell", {
            "command": "input",
            "args": ["keyevent", "KEYCODE_POWER"],
            "includeStderr": True,
            "timeout": 5000,
        })

    def set_code(self):
        self.click(self.__search_btn_locator)
        time.sleep(1)
        self.send_keys(self.__search_txt_locator,"安全")
        time.sleep(1)
        self.click(self.__search_res_locator)
        time.sleep(1)
        self.click(self.__search_res_locator)
        time.sleep(1)
        self.click(self.__code_method_locator)
        time.sleep(1)
        # print(self.get_points())
        self.drow_map(self.find_element(self.__code_map_locator))
        time.sleep(1)
        self.click(self.__config_btn_locator)
        time.sleep(1)
        self.drow_map(self.find_element(self.__code_map_locator))
        time.sleep(1)
        self.click(self.__config_btn_locator)
        time.sleep(1)
        self.click(self.__config_btn2_locator)
        time.sleep(1)
        self.driver.press_keycode(3)
        time.sleep(1)
        self.click_power()
        time.sleep(5)

    def del_code(self):
        self.click_power()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.systemui:id/notification_container_parent")')))
        time.sleep(1)
        self.driver.swipe(500,700,500,100)
        time.sleep(1)
        self.drow_map(self.find_element(self.__first_page_locator))
        time.sleep(1)
        self.click(self.__system_file_locator)
        time.sleep(1)
        self.click(self.__setting_btn_locator)
        time.sleep(1)
        self.click(self.__search_btn_locator)
        time.sleep(1)
        self.send_keys(self.__search_txt_locator, "安全")
        time.sleep(1)
        self.click(self.__search_res_locator)
        time.sleep(1)
        self.click(self.__code_method_locator)
        time.sleep(1)
        self.drow_map(self.find_element(self.__code_map_locator))
        time.sleep(1)
        self.click(self.__look_none_locator)
        time.sleep(1)
        self.click(self.__look_none_btn_locator)
        time.sleep(1)


    def run(self):
        # self.driver.back()
        self.set_code()
        time.sleep(1)
        self.del_code()
        self.close()


if __name__ == '__main__':
    setting = Setting(Setting.set_driver())
    setting.run()