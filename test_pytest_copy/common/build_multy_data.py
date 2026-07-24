import json
import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.tool import BASE_DIR, DATA_DIR


def build_multy_data():
    """从JSON文件读取乘法测试数据"""
    json_file = os.path.join(DATA_DIR, 'multy.json')

    # 如果文件不存在，返回默认测试数据
    if not os.path.exists(json_file):
        print(f"警告: 数据文件 {json_file} 不存在，使用默认数据")
        return [(1, 2, 2), (0, 5, 0), (-1, 3, -3)]

    with open(json_file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        new_list = []
        for data in data_list:
            new_list.append(tuple(data.values()))

    return new_list