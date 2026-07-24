import os
import sys

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from common.System import System


if __name__ == '__main__':
    sys = System()
    # sys.run()