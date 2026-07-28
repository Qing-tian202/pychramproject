import sys
import os
from urllib import response

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests
from typing import Optional, Union
from tools.tool import WF_HOST

session = requests.Session()

def login(username: str, password: str):
    params = {
        'username': username,
        'password': password,
    }
    response = session.post(WF_HOST + '/auth/api/login/', json=params)
    return response

def get_card_list(username,password,is_online):
    api = '/auth/api/bank-cards/'

    if is_online:
        response = login(username, password)
    else:
        response = None

    response = session.get(WF_HOST + api)

    return response

def add_card(username,password,is_online,new_card):
    api = '/auth/api/bank-cards/add/'

    if is_online:
        response = login(username, password)
    else:
        response = None

    response = session.post(WF_HOST + api, json=new_card)

    return response


# import json
#
# if __name__ == '__main__':
#     data = {
#         "username": "testuser",
#         "password": "test123456",
#         "is_online": 1,
#     }
#
#     res = get_card_list(data['username'],data['password'],data['is_online'])
#
#     print(json.dumps(res.json(), indent=4))