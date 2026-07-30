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

def get_credit_score(username: str, password: str):
    api = '/borrow/api/credit-score/'

    response = login(username, password)

    response = session.get(WF_HOST + api)

    return response

def get_quota_limit(username: str, password: str):
    api = '/borrow/api/quota/'

    response = login(username, password)

    response = session.get(WF_HOST + api)

    return response

def repayment(username: str, password: str,params):
    api = '/borrow/api/repayment/'
    response = login(username, password)

    response = session.post(WF_HOST + api, json=params)

    return response
