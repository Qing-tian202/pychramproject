import requests
from tools import *

session = requests.Session()

def get_verify_code():
    api = '/api/v0/web/authcode'

    response = session.get(ZNWL_HOST+api)

    return response


def login(username, password,auth_code):
    api = '/api/v0/web/authcode'
    res = get_verify_code()
    if not auth_code:
        auth_code = res.headers.get('auth-code')
        uuid = res.headers.get('uuid')
    else:
        uuid = ""

    data = {
        'username': username,
        'password': password,
        'auth_code': auth_code,
        'uuid': uuid
    }

    response = session.post(ZNWL_HOST+api, data=data)

    return response