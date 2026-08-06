import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from tools import DATA_DIR

def build_search():
    with open(f"{DATA_DIR}/search_data.json", 'r') as file:
        return json.load(file)



# if __name__ == '__main__':
#     sttr = '小米（MI）电视 55英寸 4K 智能WiFi网络平板 智能语音 液晶电视机 标准版 T 4A L55M5-AZ'
#     res = '小米' in sttr
#     print(res)
    # login_data = build_search()
    # print(login_data)