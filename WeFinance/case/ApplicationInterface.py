import sys
import os

from sympy import true

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


def signup(username,email,phone,password1,password2):
    api = '/auth/api/register/'

    data = {
        'username': username,
        'email': email,
        'phone': phone,
        'password1': password1,
        'password2': password2,
    }

    response = session.post(WF_HOST+api, json=data)

    return response

def logout(username, password):
    api = '/auth/api/logout/'

    response = login(username, password)
    response = session.post(WF_HOST+api)

    return response

def user_info(username,password,is_online):
    api = '/auth/api/user/'

    if is_online:
        response = login(username, password)
    else:
        response = None

    response = session.get(WF_HOST+api)

    return response


import json

# if __name__ == '__main__':
#     response = user_info('user1',
#                       '1234567890',
#                          False)
#     print(json.dumps(response.json(), indent=4))