# __init__.py

from .Logger import setup_logging
from .tool import *
from .DBTool import *

# 导出常用路径
__all__ = ['BASE_DIR', 'DATA_DIR', 'LOGS_DIR', 'RESULTS_DIR', 'ALLURE_DIR', 'TP_HOST','setup_logging', 'DBTool']