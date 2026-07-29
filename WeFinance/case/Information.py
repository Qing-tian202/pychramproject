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

def login(username, password, remember_me:Optional[Union[str, bool]] = False):
    api = '/auth/api/login/'

    data = {'username': username, 'password': password, 'remember_me': remember_me}

    response = session.post(WF_HOST+api, json=data)

    return response

def logout(username, password):
    api = '/auth/api/logout/'

    response = login(username, password)
    response = session.post(WF_HOST+api)

    return response

def get_profile(username,password,is_online):
    api = '/auth/api/profile/'

    if is_online:
        response = login(username, password)
    else:
        response = logout(username, password)

    response = session.get(WF_HOST+api)

    return response

def update_profile(username,password,is_online,data):
    api = '/auth/api/profile/update/'

    if is_online:
        response = login(username, password)
    else:
        response = logout(username, password)

    response = session.post(WF_HOST+api,json=data)

    return response