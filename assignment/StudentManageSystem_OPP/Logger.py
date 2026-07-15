import os
from datetime import datetime
import logging

def setup_logging():
    """配置日志系统"""
    # 创建日志目录
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 生成日志文件名（按日期）
    log_file = os.path.join(log_dir, f"student_system_{datetime.now().strftime('%Y%m%d')}.log")

    # 配置日志格式
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # 配置日志记录器
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),  # 写入文件
            #logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    return logging.getLogger(__name__)