import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from tools import DATA_DIR

def build_login():
    with open(f"{DATA_DIR}/login_data.json", 'r') as file:
        login_data = json.load(file)
        return list(login_data.values())


# if __name__ == '__main__':
#     login_data = build_login()
#     print(login_data)