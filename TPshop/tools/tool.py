import pathlib
import os
import sys

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# 添加项目根目录到系统路径（方便导入）
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# 也可以定义其他常用路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
ALLURE_DIR = os.path.join(BASE_DIR, 'allure_report')
TP_HOST = "http://192.168.44.137"

