"""
conftest.py - pytest 配置文件
提供全局的 fixture、钩子函数和命令行选项
"""

import pytest
import os
import sys

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tools.tool import BASE_DIR, LOGS_DIR, RESULTS_DIR
from tools.Logger import setup_logging

# 初始化日志记录器
logger = setup_logging()


def pytest_addoption(parser):
    """添加自定义命令行选项"""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        choices=["dev", "stage", "prod"],
        help="选择测试环境"
    )
    parser.addoption(
        "--quick",
        action="store_true",
        default=False,
        help="快速模式(跳过长耗时测试)"
    )
    parser.addoption(
        "--retry-count",
        action="store",
        default=0,
        type=int,
        help="测试失败后的重试次数"
    )
    parser.addini(
        "api_timeout",
        default=30,
        type="string",
        help="API请求超时时间(秒)"
    )
    parser.addini(
        "log_level",
        default="INFO",
        type="string",
        help="日志级别"
    )


@pytest.fixture(scope="session", autouse=True)
def global_setup(request):
    """全局会话级别的fixture"""
    logger.info("=" * 60)
    logger.info("测试会话开始")
    logger.info("=" * 60)

    env = request.config.getoption("--env")
    quick_mode = request.config.getoption("--quick")
    retry_count = request.config.getoption("--retry-count")
    timeout = int(request.config.getini("api_timeout"))
    log_level = request.config.getini("log_level")

    logger.info(f"测试环境: {env}")
    logger.info(f"快速模式: {quick_mode}")
    logger.info(f"重试次数: {retry_count}")
    logger.info(f"API超时: {timeout}秒")
    logger.info(f"日志级别: {log_level}")
    logger.info("-" * 60)

    print("\n========== 测试会话开始 ==========")
    print(f"测试环境: {env}")
    print(f"快速模式: {quick_mode}")
    print(f"重试次数: {retry_count}")

    yield

    logger.info("=" * 60)
    logger.info("测试会话结束")
    logger.info("=" * 60)
    print("\n========== 测试会话结束 ==========")


@pytest.fixture(scope="function", autouse=True)
def test_logger(request):
    """函数级别的fixture，记录每个测试的执行"""
    test_name = request.node.name
    test_class = request.cls.__name__ if request.cls else ""
    full_test_name = f"{test_class}.{test_name}" if test_class else test_name

    logger.info(f"\n[开始测试] {full_test_name}")
    print(f"\n[开始测试] {full_test_name}")

    import time
    start_time = time.time()

    yield

    elapsed_time = time.time() - start_time
    logger.info(f"\n[结束测试] {full_test_name}，耗时: {elapsed_time:.3f}秒")
    logger.info("-" * 40)
    print(f"\n[结束测试] {full_test_name}，耗时: {elapsed_time:.3f}秒")


def pytest_runtest_setup(item):
    """在每个测试执行前调用"""
    quick_mode = item.config.getoption("--quick")
    if quick_mode and item.get_closest_marker("slow"):
        logger.info(f"跳过慢速测试: {item.name}")
        pytest.skip("快速模式下跳过慢速测试")


def pytest_collection_modifyitems(config, items):
    """收集完测试用例后调用"""
    env = config.getoption("--env")
    logger.info(f"收集测试用例: 共 {len(items)} 个")
    print(f"\n当前测试环境: {env}，共收集到 {len(items)} 个测试用例")

    for item in items:
        item.add_marker(pytest.mark.env(env))


def pytest_configure(config):
    """pytest配置完成后调用"""
    config.addinivalue_line("markers", "slow: 标记为慢速测试")
    config.addinivalue_line("markers", "env(env): 标记测试用例适用的环境")
    config.addinivalue_line("markers", "smoke: 标记为冒烟测试")
    config.addinivalue_line("markers", "regression: 标记为回归测试")

    # 创建必要的目录
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, 'allure_report'), exist_ok=True)

    # 设置环境变量
    env = config.getoption("--env")
    os.environ["TEST_ENV"] = env

    logger.info(f"pytest 配置完成，环境: {env}")