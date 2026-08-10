import time
import re
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

def setting(driver:webdriver.Remote):
    eles = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/title")')
    ele_lst = []
    for ele in eles:
        # 提取所有数字
        numbers = re.findall(r'\d+', ele.get_attribute('bounds'))
        # 转换为 int
        numbers = [int(num) for num in numbers]
        ele_lst.append(numbers)

        print(f"{ele} 的 enabled：{ele.get_attribute('enabled')}, text:{ele.get_attribute('text')},\n"
              f"content-desc:{ele.get_attribute('content-desc')}, resource-id :{ele.get_attribute('resource-id')},\n"
              f"class:{ele.get_attribute('class')}, bounds:{numbers}")
    time.sleep(10)
    start_x = (ele_lst[0][0] + ele_lst[0][2]) // 2
    start_y = (ele_lst[0][1] + ele_lst[0][3]) // 2
    end_x = (ele_lst[-1][0] + ele_lst[-1][2]) // 2
    end_y = (ele_lst[-1][1] + ele_lst[-1][3]) // 2

    driver.tap([(start_x,start_y)],2000)
    time.sleep(5)

    driver.swipe(end_x, end_y, start_x, start_y )
    time.sleep(5)

    eles1 = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/title")')
    for ele in eles1:
        # 提取所有数字
        numbers = re.findall(r'\d+', ele.get_attribute('bounds'))
        # 转换为 int
        numbers = [int(num) for num in numbers]
        ele_lst.append(numbers)
        print(f"{ele} 的 enabled：{ele.get_attribute('enabled')}, text:{ele.get_attribute('text')},\n"
              f"content-desc:{ele.get_attribute('content-desc')}, resource-id :{ele.get_attribute('resource-id')},\n"
              f"class:{ele.get_attribute('class')}, bounds:{numbers}")

def jkchess(driver: webdriver.Remote):
    options = UiAutomator2Options()
    # options.platform_name = 'Android'
    # options.platform_version = '9'
    # options.device = 'emulator-5554'
    # options.app_package = 'com.android.settings'
    # options.app_activity = ".Settings"
    # options.no_reset = True
    options.load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        "appium:deviceName": "emulator-5554",
        "appium:appPackage": "com.tencent.jkchess",
        "appium:appWaitActivity": "*",
        "appium:unicodeKeyboard": True,
        "appium:resetKeyboard": True,
        "appium:automationName": "UiAutomator2",
        "appium:no_reset": True,
        "appium:dontStopAppOnReset": True
    })

    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.find_element(AppiumBy.ID, "com.tencent.jkchess:id/confirmBtn").click()
    time.sleep(3)

if __name__ == '__main__':
    while True:
        options = UiAutomator2Options()
        # options.platform_name = 'Android'
        # options.platform_version = '9'
        # options.device = 'emulator-5554'
        # options.app_package = 'com.android.settings'
        # options.app_activity = ".Settings"
        # options.no_reset = True
        options.load_capabilities({
          "platformName": "Android",
          "appium:platformVersion": "9.0",
          "appium:deviceName": "emulator-5554",
          "appium:appPackage": "com.android.settings",
          "appium:appActivity": ".Settings",
          "appium:unicodeKeyboard": True,
          "appium:resetKeyboard": True,
          "appium:automationName": "UiAutomator2"
        })

        driver = webdriver.Remote('http://localhost:4723',options=options)
        time.sleep(5)
        setting(driver)
        op = input("操作：quit退出：")
        driver.activate_app("com.android.settings")
        if op == "quit":
            break

    driver.quit()