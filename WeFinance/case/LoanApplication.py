import sys
import os

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


def submit_application(username,password,data):
    api = '/borrow/api/apply/'

    response = login(username, password)

    response = session.post(WF_HOST + api, json=data)

    return response

def get_my_loan_application(username,password):
    api = '/borrow/api/applications/'

    response = login(username, password)

    response = session.get(WF_HOST + api)

    return response

import json

# if __name__ == '__main__':
#     res = get_my_loan_application("newuser","NewPass123")
#     print(json.dumps(res.json(), indent=4))