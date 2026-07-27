import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import json
from tools.tool import BASE_DIR, DATA_DIR

def build_update_data():
    with open(f"{DATA_DIR}/case_data/Information/update_data.json", 'r',encoding='utf-8') as f:
        return json.load(f)
