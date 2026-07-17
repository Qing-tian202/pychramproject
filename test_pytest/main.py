import os
import pytest
from common import build_add_data
from common import build_multy_data

if __name__ == '__main__':
    pytest.main(['--alluredir=./results'])

    # --clean:清空历史数据，-o:指定输出测试报告路径
    os.system("allure generate ./results -o ./allure_report --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./allure_report")
    # print(build_multy_data())
    # print(build_add_data())
