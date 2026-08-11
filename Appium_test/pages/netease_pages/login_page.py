import time

from appium.webdriver.common.appiumby import AppiumBy

from common.base_page import BasePage
from appium import webdriver


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Remote):
        super().__init__(driver)

        # 用户名输入框
        self.__username_input_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/ph')
        # 密码输入框
        self.__password_input_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pn')
        # 忘记密码按钮
        self.__forget_pw_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pl')
        # 登录按钮
        self.__login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pp')
        # 一键登录
        self.__one_click_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pr')
        # 微信登录
        self.__wechat_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/ps')
        # 微博登录
        self.__weibo_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pt')
        # QQ登录
        self.__QQ_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/pu')
        # 小米登录
        self.__xiaomi_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/px')
        # 注册按钮
        self.__register_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/py')
        # 首页登录入口按钮
        self.__home_login_btn_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/gr')
        # 登录成功后昵称
        self.__nick_name_locator = (AppiumBy.ID, 'com.netease.newsreader.activity:id/aqq')

    def enter_username(self, username: str):
        """输入用户名
        :param username: 用户名
        """
        # self.send_keys(username, self.__username_input_locator)
        self.word_by_word_send_keys(self.__username_input_locator, username)

    def enter_password(self, password: str):
        """输入用户密码"""
        # self.send_keys(password, self.__password_input_locator)
        self.word_by_word_send_keys(self.__password_input_locator, password)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click(self.__login_btn_locator)

    def click_forget_pw(self):
        """点击忘记密码按钮"""
        self.click(self.__forget_pw_btn_locator)

    def click_register_btn(self):
        """点击注册按钮"""
        self.click(self.__register_btn_locator)

    def click_other_login_btn(self, other_login_type: int):
        """点击第三方登录按钮

        :param other_login_type: 第三方登录平台类型，取值范围：
            0 - 一键登录
            1 - 微信
            2 - 微博
            3 - QQ
            4 - 小米
        """
        match other_login_type:
            case 0:
                self.click(self.__one_click_login_btn_locator)
            case 1:
                self.click(self.__wechat_login_btn_locator)
            case 2:
                self.click(self.__weibo_login_btn_locator)
            case 3:
                self.click(self.__QQ_login_btn_locator)
            case 4:
                self.click(self.__xiaomi_login_btn_locator)

    def get_nick_name(self):
        return self.get_text(self.__nick_name_locator)

    def navigate_to_login_page(self):
        """从欢迎页面导航之登录页面"""
        # 点击返回按钮进入主页
        time.sleep(0.5)
        self.press_keycode_back()
        # 点击空白处，退出引导页面
        time.sleep(0.5)
        self.driver.tap([(500, 500)])
        time.sleep(0.5)
        self.click(self.__home_login_btn_locator)
        time.sleep(0.5)
