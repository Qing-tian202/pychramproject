# __init__.py

# 导入核心功能
from .login_service import login
from .login_service import get_login_data

# 定义公共API
__all__ = ['login','get_login_data']

# 版本信息
__version__ = '1.0.0'