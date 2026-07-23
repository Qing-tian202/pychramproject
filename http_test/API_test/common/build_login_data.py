import json
from tools import *

def build_login_data():
    with open(f"{BASE_DIR}/../data/login_data.json", 'r',encoding='utf-8') as f:
        return json.load(f)