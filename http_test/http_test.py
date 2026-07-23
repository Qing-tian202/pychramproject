import requests
import json



def try_login():
    host = 'http://192.168.44.133:80'
    url = host + '/index.php'

    params = {"m": "Home", "c": "User", "a": "do_login"}

    data = {"username": "13800138006", "password": "123456", "verify_code": "crxy"}

    # 创建一个会话对象
    session = requests.Session()
    
    # 发送GET请求获取页面
    session.get(host, params={"m": "Home", "c": "User", "a": "verify"})


    response = session.post(url, data=data, params=params)
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

if __name__ == '__main__':
    # cookie = {"PHPSESSID":"d7n04atggumlbjtrm5r2hfgj96","is_distribut":"1","user_id":"8","is_mobile":"0"}
    # response = requests.post(url,data=data,params=p,cookies=cookie)
    try_login()

