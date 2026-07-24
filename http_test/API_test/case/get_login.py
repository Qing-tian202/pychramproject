import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests
from tools.tool import ZNWL_HOST

session = requests.Session()

def get_verify_code():
    api = '/api/v0/web/authcode'

    response = session.get(ZNWL_HOST+api)

    return response


def login(username, password,auth_code):
    api = '/api/v0/web/login'
    res = get_verify_code()
    if not auth_code:
        auth_code = res.headers.get('randCode')
        uuid = res.headers.get('uuid')
    else:
        auth_code = "0000"
        uuid = "3126545874"

    data = {
        'uuid': uuid,
        'authCode': auth_code,
        'username': username,
        'password': password
    }
    print(data)

    response = session.post(ZNWL_HOST+api, json=data)

    return response

# from common.build_login_data import build_login_data
# import json
# if __name__ == '__main__':
#     for data in build_login_data():
#         #print(data)
#         res = login(data['username'],data['password'],data['authCode'])
#         print(res.json())