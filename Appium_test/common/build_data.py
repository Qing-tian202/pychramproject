import json


def build_login_data():
    with open('datas/test_login.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)

        return json_data
