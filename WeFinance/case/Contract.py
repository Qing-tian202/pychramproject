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

def logout(username, password):
    api = '/auth/api/logout/'

    response = login(username, password)
    response = session.post(WF_HOST+api)

    return response

def generate_loan_contract(username,password,params):
    api = f'/borrow/api/applications/{params.get("application_id")}/generate-contract/'

    if params.get("is_online"):
        response = login(username, password)
    else:
        response = logout(username, password)

    response = session.post(WF_HOST+api)

    return response

def signature_contract(username,password,params):

    api = f'/borrow/api/applications/{params.get("application_id")}/sign-contract/'

    response = login(username, password)

    response = session.post(WF_HOST+api,json = {"quick_sign": True})

    return response


def get_chosen_contract_info(username,password,params):
    api = f'/borrow/api/applications/{params.get("application_id")}/contract/'

    response = login(username, password)
    response = session.get(WF_HOST+api)

    return response

def get_disbursed_contract_info(username,password,params):

    api = f'/borrow/api/applications/{params.get("application_id")}/disbursement/'

    response = login(username, password)

    response = session.get(WF_HOST+api)

    return response


import json
if __name__ == '__main__':
    p = {
        "application_id":69,
        "is_online":True,
    }
    res = generate_loan_contract("testuser","test123456",p)
    print(json.dumps(res.json(), indent=4))