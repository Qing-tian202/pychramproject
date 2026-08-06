import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '9'
options.device = 'emulator-5554'
options.app_package = 'com.android.settings'
options.app_activity = ".Settings"
# options.no_reset = True

driver = webdriver.Remote('http://localhost:4723',options=options)


time.sleep(10)

driver.quit()