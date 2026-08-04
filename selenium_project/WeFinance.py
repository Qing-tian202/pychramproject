import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class WeFinance:
    def __init__(self):
        # 初始化配置
        self.executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"
        self.username = "testuser"
        self.password = "test123456"
        self.contract_number = ""
        self.host = "http://192.168.44.130:8000/"
        self.setup_driver()
        self.actions = ActionChains(self.driver)

    def setup_driver(self):
        service = Service(self.executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--window-size=1920,1080')

        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        try:
            self.driver.get(self.host) #主页
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".fas.fa-sign-in-alt").click() #跳转登录页
            time.sleep(1)
            self.actions.click(self.driver.find_element(By.ID, "id_username")).perform()
            time.sleep(1)
            self.driver.find_element(By.ID, "id_username").send_keys(self.username) #输入用户名
            time.sleep(1)
            self.actions.click(self.driver.find_element(By.ID, "password-field")).perform()
            time.sleep(1)
            self.driver.find_element(By.ID, "password-field").send_keys(self.password) #输入密码
            time.sleep(1)
            self.driver.find_element(By.ID, "id_remember_me").click() # 确认登录状态
            time.sleep(1)
            self.driver.find_element(By.ID, "submit-id-submit").click() # 登录

            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-primary.text-white.rounded-circle.d-flex.align-items-center.justify-content-center.me-2")))
            return True
        except Exception as e:
            print(f"出现错误: {e}")
            return False

    def close(self):
        self.driver.quit()

    def rock(self,rite):
        try:
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            target_position = total_height * rite  # 滚动到页面10%位置
            current_position = self.driver.execute_script("return window.pageYOffset")

            if target_position <= current_position:
                print("已在目标位置")
                return True

            # 计算滚动距离
            distance = target_position - current_position
            steps = 40  # 分成40步

            for i in range(steps):
                # 使用缓动函数让滚动更自然（先快后慢）
                progress = (i + 1) / steps
                eased_progress = 1 - (1 - progress) ** 2
                scroll_position = current_position + (distance * eased_progress)

                self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")

                # 随机停顿，模拟人类阅读
                sleep_time = random.uniform(0.03, 0.08)
                if i % 8 == 0:  # 每8步停顿稍长一点
                    sleep_time = random.uniform(0.2, 0.5)
                time.sleep(sleep_time)

            time.sleep(1)

        except Exception as e:
            print(f"滚动失败: {e}")

    def find_product(self):
        self.driver.find_element(By.ID, "productsDropdown").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".fas.fa-hand-holding-usd").click()
        time.sleep(1)
        self.rock(0.1)



    def borrow(self,purpose_value = "travel"):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.w-100").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
        time.sleep(1)
        # 等待下拉框元素加载
        purpose_select = self.wait.until(
            EC.presence_of_element_located((By.ID, "id_purpose"))
        )

        self.actions.click(purpose_select).perform()
        # 使用Select类处理下拉框
        select = Select(purpose_select)

        # 根据值选择
        select.select_by_value(purpose_value)
        time.sleep(1)

if __name__ == '__main__':
    we = WeFinance()

    if we.login():
        time.sleep(1)
        we.find_product()
        time.sleep(1)
        we.borrow()
        time.sleep(1)

        we.close()