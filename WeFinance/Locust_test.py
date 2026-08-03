# 导入Locust框架中必要的类和函数
from locust import HttpUser, constant, between, task, TaskSet, SequentialTaskSet
import json


# 定义一个任务集类，它继承自TaskSet
# TaskSet允许你定义一组相关的任务，这些任务可以在用户会话中按顺序或随机执行
class TaskTest(TaskSet):
    # 使用@task装饰器定义一个任务
    # 这个任务模拟用户的登录行为
    @task
    def login(self):
        # 定义登录接口的URL
        url = 'auth/api/login/'
        # 准备POST请求的数据，这里是一个JSON格式的用户名和密码
        json = {
            "username": "testuser",
            "password": "test123456",
            "remember_me": "true"
        }
        # 设置请求头，指定内容类型为JSON
        header = {"Content-Type": "application/json;charset=UTF-8"}
        # 使用self.client发送POST请求，client就是一个requests对象
        # method指定请求方法，url指定请求地址，json指定请求体数据，headers指定请求头
        # name参数用于在Locust的Web界面中标识这个请求，便于查看统计信息
        res = self.client.request(method='POST', url=url, json=json,
                            headers=header, name='登录',verify=False)
        #print(json.dumps(res.json(), indent=4))
        print(res.json())

# 定义一个用户类，它继承自HttpUser
# HttpUser是Locust中用于模拟HTTP用户的基类
class Login(HttpUser):
    # 设置被测系统的基地址
    host = 'http://192.168.44.130:8000/'

    # 设置用户执行请求之间的等待时间
    # 这里使用between函数生成一个1到3秒之间的随机等待时间
    # 这样可以模拟用户在实际操作中可能存在的思考时间或延迟
    # 如果使用constant函数，则所有请求之间的等待时间将是固定的
    # wait_time = constant(3)  # 每次请求停顿时间 （思考时间）
    wait_time = between(1, 3)

    # 指定用户要执行的任务集
    # 这里将TaskTest类添加到tasks列表中，表示Login用户将执行TaskTest中定义的任务
    # 注意，由于TaskTest继承自TaskSet，因此它可以包含多个任务，
    # 并且这些任务可以在用户会话中按顺序或随机执行（取决于TaskSet的具体实现）
    tasks = [TaskTest]