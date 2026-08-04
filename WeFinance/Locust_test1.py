# 导入Locust框架中必要的类和函数
import requests
from locust import HttpUser, between, task, TaskSet
from requests import Response
from random import randint


class TaskTest(TaskSet):
    """任务集类，定义用户要执行的一系列任务"""

    def __init__(self, parent):
        """初始化方法"""
        super().__init__(parent)  # 调用父类初始化
        self.new_bankcard_id = 0  # 初始化银行卡ID为0

    def on_start(self):
        """
        每个虚拟用户开始执行时的钩子函数
        在用户创建后自动执行，用于初始化操作
        """
        self.login()  # 执行登录操作
        self.add_user_bankcards()  # 添加测试用的银行卡

    def login(self):
        """用户登录方法"""
        # 定义登录接口的URL
        url = 'auth/api/login/'
        # 构造登录请求的JSON数据
        json = {
            "username": "testuser",  # 测试用户名
            "password": "test123456",  # 测试密码
            "remember_me": True  # 记住登录状态
        }

        # 设置请求头，指定内容类型为JSON
        header = {"Content-Type": "application/json;charset=UTF-8"}
        # 发送POST登录请求
        res: Response = self.client.request(method='POST', url=url, json=json,
                                            headers=header, name='登录')
        print(f'登录：{res.json()}')  # 打印登录响应结果

    @task(10)  # 任务装饰器，权重为10，表示执行频率较高
    def get_user_bankcards(self):
        """获取当前用户银行卡信息任务"""
        url = 'auth/api/bank-cards/'  # 获取银行卡列表的接口URL
        res: Response = self.client.request(method='GET', url=url,
                                            name='获取当前用户银行卡信息')
        print(res.json())  # 打印响应结果

    def add_user_bankcards(self):
        """为当前用户添加银行卡信息"""
        url = 'auth/api/bank-cards/add/'  # 添加银行卡的接口URL
        # 构造添加银行卡的请求数据
        json = {
            "bank_name": "中国工商银行",  # 银行名称
            "card_number": "6222021234567899999",  # 银行卡号
            "cardholder_name": "张三",  # 持卡人姓名
            "card_type": "debit",  # 卡片类型：借记卡
            "is_default": "true"  # 是否默认卡片
        }

        # 设置请求头，指定内容类型为JSON
        header = {"Content-Type": "application/json;charset=UTF-8"}
        # 发送POST请求添加银行卡
        res: Response = self.client.request(method='POST',
                                            headers=header, url=url,
                                            json=json, name='添加银行卡')
        # 保存新添加的银行卡ID，用于后续更新和删除操作
        # self.new_bankcard_id = res.json()['data']['card_id']
        data = res.json().get('data', {})
        # 兼容两种格式：{'card_id': 50} 或 50
        if isinstance(data, dict):
            self.new_bankcard_id = data.get('card_id')
        else:
            self.new_bankcard_id = data

    @task(5)  # 任务装饰器，权重为5，表示执行频率中等
    def update_user_bankcard_by_id(self):
        """修改银行卡信息任务"""
        # 银行名称列表，用于随机选择
        bank_names = ["中国建设银行", "中国工商银行", "中国农业银行", "中国银行"]
        # 随机选择一个银行名称
        new_bank_name = bank_names[randint(0, len(bank_names) - 1)]
        # 构造更新银行卡信息的URL，使用之前保存的银行卡ID
        url = f'auth/api/bank-cards/{self.new_bankcard_id}/update/'
        # 构造更新请求的数据，只更新银行名称
        json = {
            "bank_name": new_bank_name
        }

        # 设置请求头
        header = {"Content-Type": "application/json;charset=UTF-8"}
        # 使用catch_response=True捕获响应以便自定义成功/失败判断
        with self.client.request(method='POST', url=url, json=json,
                                 name='更新银行卡信息', catch_response=True) as resp:
            # 根据响应状态判断请求是否成功
            if resp.json()['status'] != 0:
                resp.failure("银行卡信息更新失败")  # 标记为失败请求

    def delete_user_bankcard_by_id(self):
        """根据ID删除银行卡"""
        # 构造删除银行卡的URL
        url = f'auth/api/bank-cards/{self.new_bankcard_id}/delete/'

        # 设置请求头
        header = {"Content-Type": "application/json;charset=UTF-8"}
        # 发送POST请求删除银行卡
        res: Response = self.client.request(method='POST', headers=header,
                                            url=url, name='删除银行卡')

    def logout(self):
        """用户登出方法"""
        # 定义登出接口的URL
        url = 'auth/api/logout/'
        # 发送登出请求
        res: Response = self.client.request(method='POST', url=url, name='退出登录')

    def on_stop(self):
        """
        每个虚拟用户停止执行时的钩子函数
        在用户停止前自动执行，用于清理操作
        """
        self.delete_user_bankcard_by_id()  # 删除测试用的银行卡
        self.logout()  # 执行登出操作


class Login(HttpUser):
    """虚拟用户类，定义用户行为和配置"""

    # 设置被测系统的基地址，所有请求都会基于这个地址
    host = 'http://192.168.44.130:8000/'

    # 设置用户等待时间范围，在每个任务之间随机等待1-3秒
    wait_time = between(1, 3)

    # 指定用户要执行的任务集，这里使用上面定义的TaskTest类
    tasks = [TaskTest]