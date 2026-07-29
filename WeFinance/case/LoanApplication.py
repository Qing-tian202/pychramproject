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

def get_chosen_loan_application(username,password,application_id):
    api = f'/borrow/api/applications/{application_id}/'
    response = login(username, password)

    response = session.get(WF_HOST + api)
    return response

def upload_loan_application_material(username,password,params):
    response = login(username, password)

    api = '/borrow/api/documents/upload/'

    file_path = params['file_path']
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as file:
        p = {
            "application_id": (None,str(params['application_id'])),
            "document_type": (None,params['document_type']),
            "file": (file_name,file,"image/jpeg")
        }
        response = session.post(WF_HOST + api, files=p)
        return response

import json

# if __name__ == '__main__':
#     param = {
#         'application_id': 70,
#         'document_type': "id_card",
#         'file_path':'C:/Users/test37/Desktop/work/data.txt'
#     }
#     res = upload_loan_application_material("testuser","test123456",param)
#     print(json.dumps(res.json(), indent=4))