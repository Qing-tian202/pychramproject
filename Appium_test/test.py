import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.power import Power
from selenium.webdriver import ActionChains

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '9'
options.device = 'emulator-5554'
# options.app_wait_activity = ".Settings"
# options.app_package = 'com.android.settings'
# options.app_activity = ".Settings"
options.app_package = 'com.netease.newsreader.activity'
options.app_activity = "com.netease.nr.biz.ad.AdActivity"
options.auto_grant_permissions = True
options.set_capability("unicodeKeyboard", True)
options.set_capability("resetKeyboard", True)

# options.platform_name
options.no_reset = True
#
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

driver.launch_app()

# driver.send_sms("555-123-4567", "你好，重庆！")


# def shell(driver, command, args=list[str] | str, timeout=5000, include_stderr=True):
#     """
#     简化版 mobile:shell 调用
#     :param driver: Appium WebDriver
#     :param command: shell 命令，如 'pm', 'am', 'input'
#     :param args: list[str]，如 ['list', 'packages'];或者 "pm list packages"
#     :param timeout: 毫秒
#     :param include_stderr: 是否返回 stderr
#     """
#     payload = {
#         "command": command,
#         "includeStderr": include_stderr,
#         "timeout": timeout,
#     }
#     print(type(args))
#     if type(args) is list:
#         payload["args"] = args
#     elif type(args) is str:
#         payload["args"] = args.split()
#     else:
#         raise TypeError('args参数类型异常')
#
#     return driver.execute_script("mobile: shell", payload)
#
#
# print(shell(driver, 'pm', "list packages"))
# print(shell(driver, 'pm', ["list", "packages"]))

#
# time.sleep(2)
# driver.current_activity
# driver.press_keycode(4)
# time.sleep(2)
# driver.tap([(500,500)])
# time.sleep(2)
# driver.find_element(AppiumBy.ID, "com.netease.newsreader.activity:id/gr").click()
# time.sleep(2)
# # driver.AC_OFF
#
#
# actions = ActionChains(driver)
# actions1 = ActionChains(driver)
#
# username_ele = driver.find_element(AppiumBy.ID, 'com.netease.newsreader.activity:id/ph')
# # username_ele.send_keys("admin@163.com")
# username_ele.clear()
# actions.click(username_ele)
# for char in "admin@163.com":
#     actions.send_keys(char).pause(1)
# # print(actions)
# actions.perform()
#
# # actions.click(username_ele).send_keys('admin@163.com').perform()
# driver.press_keycode(4)
# # time.sleep(2)
# #
# # # actions.reset_actions()
# pwd_ele = driver.find_element(AppiumBy.ID, 'com.netease.newsreader.activity:id/pn')
# # pwd_ele.click()
# # pwd_ele.send_keys('123456')
# # pwd_ele.click()
# actions1.click(pwd_ele).pause(2).send_keys('123456').perform()

# driver.tap([(0,500)])
#
# # username_ele.send_keys('admin@163.com')
# time.sleep(2)
# pwd_ele.send_keys('123456')

# print(driver.current_activity)
# driver.find_element(AppiumBy.ID, "com.android.settings:id/search_action_bar").click()
# ele = driver.find_element(AppiumBy.ID, "android:id/search_src_text")
# # ele.send_keys('a')
# for char in "admin":
#     time.sleep(1)
#     ele.send_keys(char)


time.sleep(10)

driver.quit()
