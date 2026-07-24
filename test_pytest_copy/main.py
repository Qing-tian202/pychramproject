import os
import sys
import pytest

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tools.tool import BASE_DIR, RESULTS_DIR, ALLURE_DIR

if __name__ == '__main__':
    # 确保目录存在
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(ALLURE_DIR, exist_ok=True)

    # 运行测试
    pytest.main([
        'case/',
        '-v',
        '-s',
        f'--alluredir={RESULTS_DIR}',
        '--clean-alluredir'  # 清空之前的报告
    ])

    # 生成Allure报告
    os.system(f"allure generate {RESULTS_DIR} -o {ALLURE_DIR} --clean")
    os.system("allure open -h 127.0.0.1 -p 8883 ./allure_report")