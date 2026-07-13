def login(username, passwd, security_code):
    if username == 'admin' and passwd == '123456' and security_code == '8888':
        return True
    else:
        return False


def get_login_data():
    lst = [('admin', '123456', '8888', True), ('user', 'password', '1234', False), ('admin', '123458', '8888', False),
           ('admin1', '123456', '8888', True)]
    return lst