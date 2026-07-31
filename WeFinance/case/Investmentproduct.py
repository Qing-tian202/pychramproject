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

def get_investment_products_list(params):
    api = '/investments/api/products/'

    response = session.get(WF_HOST + api, params=params)

    return response

def get_investment_info(product_id):
    api = f'/investments/api/products/{product_id}/'

    response = session.get(WF_HOST + api)

    return response