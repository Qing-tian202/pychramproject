import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Prompt():
    def __init__(self):
        # 初始化配置
        self.executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"

    def setup_driver(self):
        service = Service(self.executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--window-size=1920,1080')

        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def test(self,sttr):
        self.driver.get("https://sahitest.com/demo/promptTest.htm")

        self.driver.find_element(By.NAME, "b1").click()
        time.sleep(2)

        self.driver.switch_to.alert.send_keys(sttr)
        time.sleep(2)

        self.driver.switch_to.alert.accept()
        time.sleep(2)

        self.driver.switch_to.default_content()
        time.sleep(2)

        self.driver.find_element(By.NAME, "t1").clear()
        time.sleep(2)


    def close(self):
        self.driver.quit()


if __name__ == '__main__':
    prompt = Prompt()
    prompt.setup_driver()

    while True:
        sttr = input("input your prompt(quit to end the prompt):")
        if sttr == "quit":
            prompt.close()
            break
        prompt.test(sttr)

