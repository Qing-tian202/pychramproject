import os
import sys

# 获取项目根目录（test_pytest目录）
# __file__ 是当前文件路径：D:/pycharmproject/Python_Project/test_pytest/tools/tool.py
# os.path.dirname(__file__) 得到：D:/pycharmproject/Python_Project/test_pytest/tools
# 再取一次dirname得到项目根目录：D:/pycharmproject/Python_Project/test_pytest
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加项目根目录到系统路径（方便导入）
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# 也可以定义其他常用路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
ALLURE_DIR = os.path.join(BASE_DIR, 'allure_report')

# 导出常用路径
__all__ = ['BASE_DIR', 'DATA_DIR', 'LOGS_DIR', 'RESULTS_DIR', 'ALLURE_DIR']