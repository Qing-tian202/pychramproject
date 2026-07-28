import sys
import os
from random import seed
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

def submit_real_name(username,password,form_data):

    response = login(username,password)

    api = '/auth/api/verification/submit/'

    # 获取数据
    real_name = form_data.get('real_name')
    id_number = form_data.get('id_number')
    front_path = form_data.get('id_front')
    back_path = form_data.get('id_back')
    id_front_image_type = form_data.get('id_front_image')
    id_back_image_type = form_data.get('id_back_image')

    # 准备文件
    with open(front_path, 'rb') as front_file, \
            open(back_path, 'rb') as back_file:
        # 方式一：使用 files 参数（推荐）
        multipart_data = {
            # 文本字段
            'real_name': ('', real_name),
            'id_number': ('', id_number),

            # 文件字段
            'id_front_image': ('id_front.jpg', front_file, id_front_image_type),
            'id_back_image': ('id_back.jpg', back_file, id_back_image_type),
        }

        response = session.post(WF_HOST + api, files=multipart_data)

    return response

def get_real_name_info(username,password):
    response = login(username,password)

    api = '/auth/api/verification/status/'

    response = session.get(WF_HOST + api)

    return response

def photo_image(username,password):
    response = login(username,password)

    api = '/auth/api/avatar/'

    response = session.get(WF_HOST + api)

    return response

def change_photo(username,password,avatar_path,image_type):
    response = login(username,password)

    api = '/auth/api/avatar/update/'

    image_name = os.path.basename(avatar_path)
    print(image_name)

    with open(avatar_path, 'rb') as avatar_file:
        files = {'avatar': (image_name, avatar_file,image_type)}

        response = session.post(WF_HOST + api, files=files)

    return response


# import json
#
# if __name__ == '__main__':
#     # data = {
#     #     "real_name":"张三",
#     #     "id_number":"110101199001011234",
#     #     "id_front":"C:/Users/test37/Pictures/ji.jpg",
#     #     "id_back":"C:/Users/test37/Pictures/jinnaluo.jpg",
#     #     "id_front_image":"image/jpeg",
#     #     "id_back_image":"image/jpeg",
#     # }
#
#     response = change_photo("newuser","NewPass123","C:/Users/test37/Pictures/ji.jpg","image/jpeg")
#
#     print(json.dumps(response.json(), indent=4))