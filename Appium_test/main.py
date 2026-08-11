import os
from tools import get_current_time
import pytest

if __name__ == '__main__':
    result_path = f'reports/results/{get_current_time()}'
    report_path = f'reports/{get_current_time()}'
    pytest.main([f"--clean-alluredir", f"--alluredir=reports/results/{get_current_time()}"])
    os.system(f"allure generate {result_path} -o {report_path}")
    os.system(f"allure open {report_path} -h 127.0.0.1 -p 8883")