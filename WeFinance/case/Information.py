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

def get_profile(username,password,is_online):
    api = '/auth/api/profile/'

    if is_online:
        response = session.post(WF_HOST+'/auth/api/login/',json={'username':username,'password':password})
    else:
        response = None

    response = session.get(WF_HOST+api)

    return response