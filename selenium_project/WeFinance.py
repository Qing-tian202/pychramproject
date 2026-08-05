import random
import time
import re
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
        self.contract_page = ""
        self.host = "http://192.168.44.130:8000/"
        self.myhost = "http://192.168.47.136:8000/"
        self.setup_driver()
        self.actions = ActionChains(self.driver)

    def setup_driver(self):
        service = Service(self.executable_path)
        options = webdriver.ChromeOptions()
        options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--start-maximized')

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
        self.rock(0.15)



    def borrow(self,purpose_value = "travel"):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.w-100").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
        time.sleep(1)
        # 等待下拉框元素加载
        purpose_select = self.wait.until(
            EC.presence_of_element_located((By.ID, "id_purpose"))
        )

        purpose_select.click()
        time.sleep(1)
        option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"option[value='{purpose_value}']"))
        )
        option.click()
        time.sleep(1)

        self.driver.find_element(By.ID, "id_amount").send_keys("3000")
        time.sleep(1)

        self.driver.find_element(By.ID, "id_purpose_detail").send_keys("旅游消费")
        time.sleep(1)

        self.rock(0.3)
        # 等待下拉框元素加载
        purpose_select = self.wait.until(
            EC.presence_of_element_located((By.ID, "id_profession"))
        )

        purpose_select.click()
        time.sleep(1)
        option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='civil_servant']"))
        )
        option.click()
        time.sleep(1)

        self.driver.find_element(By.ID, "id_work_years").clear()
        self.driver.find_element(By.ID, "id_work_years").send_keys("3")
        time.sleep(1)

        self.driver.find_element(By.ID, "id_company_name").send_keys("天堂旅行团")
        time.sleep(1)

        self.driver.find_element(By.ID, "id_monthly_income").send_keys("20000")
        time.sleep(1)

        self.rock(0.5)
        self.driver.find_element(By.ID, "id_contact_name").send_keys("尼古拉斯.赵四")
        time.sleep(1)

        self.driver.find_element(By.ID, "id_contact_phone").send_keys("13800138006")
        time.sleep(1)

        self.driver.find_element(By.ID, "id_contact_relation").send_keys("兄弟")
        time.sleep(1)

        self.driver.find_element(By.ID, "creditAuth").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".fas.fa-paper-plane").click()

    def submit_material(self):
        alert_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-success"))
        )
        alert_text = alert_element.text

        # 使用正则表达式提取编号
        # 匹配格式：JK + 数字 + 字母组合
        pattern = r'JK\d{8}[A-Z0-9]+'
        self.contract_number = re.search(pattern, alert_text).group(0)
        # print(self.contract_number)

        self.rock(0.5)
        self.driver.find_element(By.ID, "bank_statement").send_keys(r"C:\Users\test37\Pictures\ji.jpg")
        time.sleep(1)
        self.driver.find_element(By.ID, "income_proof").send_keys(r"C:\Users\test37\Pictures\jinnaluo.jpg")
        time.sleep(1)
        self.rock(0.6)
        self.driver.find_element(By.ID, "submit-application").click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.contract_page = self.driver.current_url

    def pass_submit(self):
        self.driver.get(url = f"{self.host}admin-panel/")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".fas.fa-file-invoice-dollar.me-2").click()
        time.sleep(1)

        # 推荐使用的方式
        xpath = f"//h6[contains(text(), '{self.contract_number}')]/../..//a"
        self.driver.find_element(By.XPATH, xpath).click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-action.btn-approve").click()
        time.sleep(1)

        self.driver.find_element(By.ID, "review_notes").send_keys("通过")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        time.sleep(1)

        self.driver.switch_to.alert.accept()
        time.sleep(5)


    def generate_loan_contract(self):
        self.driver.get(self.contract_page)
        time.sleep(1)

        self.rock(0.5)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-sm").click()
        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-sm").click()
        time.sleep(1)

        # 1. 等待Canvas加载
        canvas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "signatureCanvas"))
        )

        # 2. 滚动到Canvas位置
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", canvas)
        time.sleep(0.5)

        # 3. 获取Canvas尺寸
        canvas_width = canvas.get_attribute('width')
        canvas_height = canvas.get_attribute('height')

        # 4. 使用ActionChains（注意偏移量不能超过Canvas边界）
        actions = ActionChains(self.driver)

        # 移动到Canvas中心偏左位置
        actions.move_to_element(canvas)
        actions.move_by_offset(10, 10)
        actions.click_and_hold()

        # 小步移动，确保不超出边界
        step_x = 10
        step_y = 15

        # 向下绘制
        for i in range(10):
            if i % 2 == 0:
                actions.move_by_offset(step_x, -step_y)
            else:
                actions.move_by_offset(step_x, step_y)
            time.sleep(0.01)

        actions.release()
        actions.perform()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".form-check-input").click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.ms-2").click()
        time.sleep(1)

        self.driver.switch_to.alert.accept()
        time.sleep(5)

    def get_message(self):
        # self.driver.get("http://192.168.44.130:8000/borrow/status/82/")
        time.sleep(3)
        ele = self.driver.find_element(By.CSS_SELECTOR, ".nav-link.dropdown-toggle.d-flex.align-items-center")
        ele.click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".fas.fa-envelope").click()
        time.sleep(1)

        # self.rock(0.3)
        self.driver.find_element(By.XPATH, f"//p[contains(text(), '{self.contract_number}')]/..//div/div/div/button[1]").click()
        time.sleep(1)



    def run(self):
        if self.login():
            time.sleep(1)
            self.find_product()
            time.sleep(1)
            self.borrow()
            time.sleep(1)
            self.submit_material()
            time.sleep(5)
            self.pass_submit()
            time.sleep(1)
            self.generate_loan_contract()
            time.sleep(1)
            self.get_message()
            time.sleep(1)

            self.close()


if __name__ == '__main__':
    we = WeFinance()
    we.run()