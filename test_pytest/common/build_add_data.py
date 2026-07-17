import json
import os
from tools import BASE_DIR

def build_add_data():
    json_file = os.path.join(f"{BASE_DIR}\..\data/add.json")
    with open(json_file) as f:
        data_list = json.load(f)  # [{}, {}, {}] ----> [(), ()]
        new_list = []
        for data in data_list:  # data 字典
            # 字典中的值，是否都需要
            new_list.append(tuple(data.values()))

    return new_list