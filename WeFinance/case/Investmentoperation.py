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

def login(username,password):
    api = '/auth/api/login/'

    data = {'username': username, 'password': password}

    response = session.post(WF_HOST + api, json=data)

    return response

def invest(username,password,params):
    api = '/investments/api/invest/'

    login(username,password)

    response = session.post(WF_HOST + api, json=params)

    return response

def get_invest_list(username,password):
    api = '/investments/api/my/'

    login(username,password)
    response = session.get(WF_HOST + api)

    return response

def get_my_invest_info(username,password,params):
    api = f'/investments/api/{params.get("investment_id")}/'

    login(username,password)
    response = session.get(WF_HOST + api)

    return response

def get_investments_summary(username,password):
    api = '/investments/api/statistics/'
    login(username,password)
    response = session.get(WF_HOST + api)

    return response