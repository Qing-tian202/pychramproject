import os
from datetime import datetime
import logging
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 使用相对导入或直接定义BASE_DIR
from tools.tool import BASE_DIR, LOGS_DIR

def setup_logging():
    """配置日志系统"""
    # 使用统一的日志目录
    log_dir = LOGS_DIR
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 生成日志文件名（按日期）
    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y%m%d')}.log")

    # 配置日志格式
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # 清除已有的handler（避免重复）
    root_logger = logging.getLogger()
    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    # 配置日志记录器
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # 同时输出到控制台，方便调试
        ]
    )

    return logging.getLogger(__name__)