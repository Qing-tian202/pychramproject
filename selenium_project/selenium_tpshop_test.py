# 完整的DeepSeek API测试脚本
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TPshopTester:
    def __init__(self):
        # 初始化配置
        self.executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"
        self.username = "13800138010"
        self.password = "123456"
        self.verify_code = "crxy"

    def setup_driver(self):
        service = Service(self.executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--window-size=1920,1080')

        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def sign_up(self):
        """注册"""
        try:
            self.driver.get("http://192.168.44.135/Home/user/reg.html")
            time.sleep(2)

            self.driver.find_element(By.ID, "username").send_keys(self.username)
            time.sleep(3)
            self.driver.find_element(By.NAME, "verify_code").send_keys(self.verify_code)
            time.sleep(3)
            self.driver.find_element(By.ID, "password").send_keys(self.password)
            time.sleep(3)
            self.driver.find_element(By.ID, "password2").send_keys(self.password)
            time.sleep(3)
            self.driver.find_element(By.CSS_SELECTOR,".regbtn").click()
            time.sleep(3)

            self.driver.refresh()
            time.sleep(3)

            print(" 注册成功")
            return True
        except Exception as e:
            print(f"注册失败: {e}")
            return False

    def login(self):
        """登录"""
        try:
            self.driver.get("http://192.168.44.135/Home/user/login.html")
            time.sleep(2)

            self.driver.find_element(By.ID, "username").send_keys(self.username)
            time.sleep(3)
            self.driver.find_element(By.ID, "password").send_keys(self.password)
            time.sleep(3)
            self.driver.find_element(By.NAME, "verify_code").send_keys(self.verify_code)
            time.sleep(3)
            self.driver.find_element(By.NAME, "sbtbutton").click()

            self.driver.refresh()
            time.sleep(3)

            print("登录成功")
        except Exception as e:
            print(f"登录失败: {e}")

    def logout(self, flags=True):
        if flags:
            self.driver.find_element(By.CSS_SELECTOR,"a[title='退出']").click()
        else:
            self.driver.find_element(By.CSS_SELECTOR,"a[href *= 'logout']").click()
        time.sleep(3)

    def close(self):
        self.driver.quit()

    def goods(self,goods_name):
        self.driver.find_element(By.ID,"q").send_keys(goods_name) #查找商品

        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR,".search_usercenter_btn").click() #确认搜索
        time.sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, "a[onclick*='AjaxAddCart']").click() #点击选中商品
        time.sleep(10)

        self.driver.find_element(By.ID,"join_cart").click() #添加购物车
        time.sleep(3)

        self.driver.switch_to.frame("layui-layer-iframe1")#切换iframe
        self.driver.find_element(By.CSS_SELECTOR, ".ui-button.ui-button-122.fl").click() #进入购物车
        time.sleep(3)

        self.driver.switch_to.default_content() #返回主界面
        self.driver.find_element(By.CSS_SELECTOR, ".deleteGoods.deleteItem").click() #选择商品删除
        time.sleep(3)

        self.driver.find_element(By.ID, "removeGoods").click() #确认删除
        time.sleep(3)


if __name__ == "__main__":
    tester = TPshopTester()
    tester.setup_driver()

    # tester.login()
    #
    # tester.goods("vivo")
    #
    # tester.close()

    if tester.sign_up():
        tester.logout()
        time.sleep(3)

        tester.login()

        tester.goods("vivo")

        tester.close()