from service import login
from service import get_login_data


if __name__ == "__main__":
    try:
        print("begin test!")
        for name,passwd,security_code,expected in get_login_data():
            assert(login(name,passwd,security_code) == expected)
        print("test pass!")
    except Exception as e:
        print("test not pass")