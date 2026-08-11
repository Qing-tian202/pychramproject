import pathlib
from datetime import datetime

# 定义工程路径
BASE_PATH = pathlib.Path(__file__).parent.parent.absolute()
# Appium服务默认地址
APPIUM_SERVER = "http://127.0.0.1:4723"


def get_current_time():
    """获取当前时间"""
    return datetime.now().strftime("%Y%m%d%H%M%S")
