import json
import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.tool import BASE_DIR, DATA_DIR

def build_login_data():
    with open(f"{DATA_DIR}/login_data.json", 'r',encoding='utf-8') as f:
        return json.load(f)