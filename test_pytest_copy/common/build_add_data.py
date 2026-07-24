import json
import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.tool import BASE_DIR, DATA_DIR


def build_add_data():
    """从JSON文件读取加法测试数据"""
    json_file = os.path.join(DATA_DIR, 'add.json')

    # 如果文件不存在，返回默认测试数据
    if not os.path.exists(json_file):
        print(f"警告: 数据文件 {json_file} 不存在，使用默认数据")
        return [(1, 2, 3), (0, 0, 0), (-1, 1, 0)]

    with open(json_file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        new_list = []
        for data in data_list:
            # 提取字典中的所有值作为元组
            new_list.append(tuple(data.values()))

    return new_list