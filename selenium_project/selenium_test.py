# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 2.创建浏览器驱动对象
# Firefox浏览器：
# driver = webdriver.Firefox()
# Chrome浏览器：

# 指定ChromeDriver的路径
executable_path = r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe"

# 创建一个Service对象，并传递ChromeDriver的路径
service = Service(executable_path=executable_path)

# options：指的是 Selenium 中的 ChromeOptions（或 EdgeOptions）对象，用来定制浏览器的启动参数。
options = webdriver.ChromeOptions()

# 方式1：直接指定
options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"

# 下面皆是反检测爬虫机制
# 禁用 blink 的 AutomationControlled 特征，JS可以通过navigator判断是否为爬虫
options.add_argument('--disable-blink-features=AutomationControlled')
# 禁止显示网页上方“收到自动化软件控制”，并禁止显示部分内部变量
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=service, options=options)
# 上面这种写法是可以成功运行的，但是前提是必须把chrome.exe与python.exe放在同一个目录下，
# 并且在系统环境变量的PATH里面添加该路径

# 3.打开Web页面
driver.get("http://www.baidu.com/")

driver.find_element(By.ID, "chat-textarea").send_keys("北京")
time.sleep(3)
driver.find_element(By.ID, "chat-submit-button").click()

# 4.暂停
time.sleep(10)
# 5.关闭驱动对象
driver.quit()
