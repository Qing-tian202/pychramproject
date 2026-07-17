"""
conftest.py - pytest 配置文件
提供全局的 fixture、钩子函数和命令行选项
"""

import pytest
import os
from tools.tool import BASE_DIR
from common import *
from scripts import setup_logging

# 初始化日志记录器
logger = setup_logging()


def pytest_addoption(parser):
    """
    pytest 钩子函数：添加自定义命令行选项和 ini 配置项

    该函数在 pytest 启动时被调用，用于扩展 pytest 的命令行参数和配置文件选项
    """

    # ---------- 命令行选项 ----------

    # 添加 --env 选项：用于选择测试环境
    parser.addoption(
        "--env",  # 命令行参数名称
        action="store",  # 存储动作：存储用户输入的值
        default="dev",  # 默认值
        choices=["dev", "stage", "prod"],  # 可选值列表
        help="选择测试环境，可选值: dev(开发), stage(预发布), prod(生产)"
    )

    # 添加 --quick 选项：快速模式开关
    parser.addoption(
        "--quick",  # 命令行参数名称
        action="store_true",  # 存储动作：存在则为 True，否则为 False
        default=False,  # 默认值：不启用快速模式
        help="快速模式(跳过长耗时测试)"
    )

    # 添加 --retry-count 选项：失败重试次数
    parser.addoption(
        "--retry-count",  # 命令行参数名称
        action="store",  # 存储动作：存储用户输入的值
        default=0,  # 默认值
        type=int,  # 参数类型：整数
        help="测试失败后的重试次数，默认为0"
    )

    # ---------- ini 配置项 ----------

    # 添加 api_timeout 配置项：API 请求超时时间
    parser.addini(
        "api_timeout",  # ini 配置项名称
        default=30,  # 默认值
        type="int",  # 配置项类型：整数
        help="API请求超时时间(秒)"
    )

    # 添加 log_level 配置项：日志级别
    parser.addini(
        "log_level",  # ini 配置项名称
        default="INFO",  # 默认值
        type="string",  # 配置项类型：字符串
        help="日志级别，可选: DEBUG, INFO, WARNING, ERROR"
    )


# ---------- 全局 Fixture ----------

@pytest.fixture(scope="session", autouse=True)
def global_setup(request):
    """
    全局级别的 fixture：在所有测试开始前执行一次，结束后执行一次
    scope="session" 表示会话级别，整个测试会话只执行一次
    autouse=True 表示自动应用，无需显式引用
    """
    logger.info("=" * 60)
    logger.info("测试会话开始")
    logger.info("=" * 60)

    # 获取命令行选项的值
    env = request.config.getoption("--env")
    quick_mode = request.config.getoption("--quick")
    retry_count = request.config.getoption("--retry-count")

    # 获取 ini 配置项的值
    timeout = request.config.getini("api_timeout")
    log_level = request.config.getini("log_level")

    # 记录配置信息到日志
    logger.info(f"测试环境: {env}")
    logger.info(f"快速模式: {quick_mode}")
    logger.info(f"重试次数: {retry_count}")
    logger.info(f"API超时: {timeout}秒")
    logger.info(f"日志级别: {log_level}")
    logger.info("-" * 60)

    # 同时打印到控制台（方便查看）
    print("\n========== 测试会话开始 ==========")
    print(f"测试环境: {env}")
    print(f"快速模式: {quick_mode}")
    print(f"重试次数: {retry_count}")
    print(f"API超时: {timeout}秒")
    print(f"日志级别: {log_level}")

    # yield 之前的代码在测试开始前执行
    yield

    # yield 之后的代码在测试结束后执行
    logger.info("=" * 60)
    logger.info("测试会话结束")
    logger.info("=" * 60)
    print("\n========== 测试会话结束 ==========")


@pytest.fixture(scope="function", autouse=True)
def test_logger(request):
    """
    函数级别的 fixture：在每个测试函数执行前后记录日志
    scope="function" 表示函数级别，每个测试函数都会执行
    autouse=True 表示自动应用到所有测试函数
    """
    test_name = request.node.name
    test_class = request.cls.__name__ if request.cls else ""

    # 构建完整的测试名称
    full_test_name = f"{test_class}.{test_name}" if test_class else test_name

    # 记录测试开始
    logger.info(f"[开始测试] {full_test_name}")
    print(f"\n[开始测试] {full_test_name}")

    # 获取测试函数执行时间
    import time
    start_time = time.time()

    # yield 之前的代码在测试执行前执行
    yield

    # yield 之后的代码在测试执行后执行
    elapsed_time = time.time() - start_time

    # 记录测试结束及耗时
    logger.info(f"[结束测试] {full_test_name}，耗时: {elapsed_time:.3f}秒")
    logger.info("-" * 40)
    print(f"[结束测试] {full_test_name}，耗时: {elapsed_time:.3f}秒")


# ---------- 自定义插件/钩子 ----------

def pytest_runtest_setup(item):
    """
    pytest 钩子函数：在每个测试项（测试用例）执行前调用
    可以用于动态跳过某些测试用例
    """
    # 获取 quick 模式配置
    quick_mode = item.config.getoption("--quick")

    # 如果启用了快速模式，并且测试用例标记了 @pytest.mark.slow
    if quick_mode and item.get_closest_marker("slow"):
        # 跳过标记为 slow 的测试用例
        logger.info(f"跳过慢速测试: {item.name}")
        pytest.skip("快速模式下跳过慢速测试")


def pytest_collection_modifyitems(config, items):
    """
    pytest 钩子函数：在收集完所有测试用例后调用
    可以用于修改、排序或过滤测试用例
    """
    # 获取环境配置
    env = config.getoption("--env")

    # 记录收集到的测试用例数量
    logger.info(f"收集测试用例: 共 {len(items)} 个")
    print(f"\n当前测试环境: {env}，共收集到 {len(items)} 个测试用例")

    # 为所有测试用例添加环境标记（方便过滤）
    for item in items:
        # 添加自定义标记
        item.add_marker(pytest.mark.env(env))

    # item.name: 测试名称（函数名）
    # item.nodeid: 完整节点ID（如 "path/to/test_file.py::TestClass::test_method"）
    # item.keywords: 测试的标记（markers）集合
    # item.module: 测试所在的模块
    # item.cls: 测试所在的类（如果有）
    # item.function: 测试函数对象
    # item.add_marker：动态添加标记


def pytest_configure(config):
    """
    pytest 钩子函数：在 pytest 配置完成后调用
    用于注册自定义标记
    """
    # 注册自定义标记，避免 warnings
    config.addinivalue_line("markers", "slow: 标记为慢速测试")
    config.addinivalue_line("markers", "env(env): 标记测试用例适用的环境")
    config.addinivalue_line("markers", "smoke: 标记为冒烟测试")
    config.addinivalue_line("markers", "regression: 标记为回归测试")

    # 创建测试结果目录
    os.makedirs(f"{BASE_DIR}\..\test-results", exist_ok=True)

    # 动态修改选项值 --log_level值
    config.option.log_level = "DEBUG"

    # 设置环境变量
    env = config.getoption("--env")
    os.environ["TEST_ENV"] = env

    logger.info(f"pytest 配置完成，环境: {env}")


@pytest.fixture(scope='function', params=build_add_data(), autouse=True)
def define_fixture(request):
    """
    数据驱动 fixture：为测试函数提供参数化的测试数据
    scope='function' 表示每个测试函数都会使用不同的参数
    params=get_data() 从 tool.py 获取测试数据
    autouse=True 自动应用到所有测试函数
    """
    # 获取当前测试数据
    test_data = request.param
    x, y, expected = test_data

    # 记录 fixture 设置信息
    logger.debug(f"Fixture 设置: 输入数据 x={x}, y={y}, 期望结果={expected}")
    print(f'\n[Fixture] 设置测试数据: x={x}, y={y}, expect={expected}')

    # yield 返回测试数据
    yield test_data

    # fixture 清理
    logger.debug(f"Fixture 清理: 完成测试数据 x={x}, y={y}")
    print(f'[Fixture] 清理测试数据完成')