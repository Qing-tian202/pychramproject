import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Iterable,Generator

import allure
import pytest
import yaml
from _pytest.config import Config
from _pytest.main import Session
from _pytest.nodes import Collector, Item, Node
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from common import BasePage
from tools import TP_HOST,setup_logging,LOGS_DIR


# 全局logger实例
test_logger = setup_logging()


# ==================== Fixture 定义 ====================
@pytest.fixture(scope="session")
def chrome_driver() -> Generator[webdriver.Chrome, None, None]:
    """创建Chrome浏览器驱动"""
    test_logger.info(" 启动Chrome浏览器 (Session级别)")
    try:
        service = Service(executable_path=r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 可选：添加无头模式
        # options.add_argument('--headless')

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        test_logger.info(" Chrome浏览器启动成功")

        yield driver

        test_logger.info(" 关闭Chrome浏览器")
        driver.quit()
        test_logger.info(" Chrome浏览器已关闭")
    except Exception as e:
        test_logger.error(f" 浏览器启动失败: {e}", exc_info=True)
        raise


@pytest.fixture(scope="function")
def base_page(chrome_driver) -> Generator[BasePage, None, None]:
    """创建BasePage实例，每个测试函数使用独立的实例"""
    test_logger.info(" 创建BasePage实例")
    page = BasePage(chrome_driver)
    yield page
    # 测试完成后清理
    try:
        chrome_driver.delete_all_cookies()
        test_logger.info(" Cookies已清除")
    except Exception as e:
        test_logger.warning(f"清理Cookies失败: {e}")


# ==================== 测试收集 ====================
def pytest_collect_file(file_path: Path, parent: Collector) -> Collector | None:
    if file_path.suffix == '.yaml' and file_path.parent.name == 'data':
        test_logger.info(f"发现测试数据文件: {file_path}")
        return YamlFile.from_parent(parent=parent, path=file_path)


# ==================== 失败截图钩子 ====================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """当测试失败时自动截图并记录日志"""
    # 记录测试开始
    if call.when == "setup":
        test_logger.info(f"========== 开始执行测试: {item.nodeid} ==========")

    # 执行测试
    outcome = yield
    report = outcome.get_result()

    # 记录测试结果
    if call.when == "call":
        if report.passed:
            test_logger.info(f" 测试通过: {item.nodeid}")
        elif report.failed:
            test_logger.error(f" 测试失败: {item.nodeid}")
            test_logger.error(f"失败原因: {report.longrepr}")

            # 截图处理
            if isinstance(item, YamlItem):
                try:
                    page = getattr(item, 'page', None)
                    if page and hasattr(page, 'driver'):
                        # 确保截图目录存在
                        screenshot_dir = Path(LOGS_DIR / "screenshots")
                        screenshot_dir.mkdir(exist_ok=True)

                        # 生成截图文件名
                        timestamp = time.strftime("%Y%m%d_%H%M%S")
                        screenshot_name = f"screenshot_{item.name}_{timestamp}.png"
                        screenshot_path = screenshot_dir / screenshot_name

                        # 保存截图
                        page.driver.save_screenshot(str(screenshot_path))
                        test_logger.info(f" 截图已保存: {screenshot_path}")

                        # 记录失败时的页面信息
                        test_logger.info(f"当前URL: {page.driver.current_url}")
                        test_logger.info(f"页面标题: {page.driver.title}")
                        test_logger.info(f"失败步骤: {getattr(item, 'current_step_name', '未知步骤')}")

                        # 附加到 Allure
                        allure.attach.file(
                            str(screenshot_path),
                            name=f"失败截图 - {item.name}",
                            attachment_type=allure.attachment_type.PNG
                        )

                        # 附加失败上下文信息
                        context_info = [
                            f"测试用例: {item.name}",
                            f"失败步骤: {getattr(item, 'current_step_name', '未知步骤')}",
                            f"步骤索引: {getattr(item, 'current_step_index', -1)}",
                            f"当前URL: {page.driver.current_url}",
                            f"页面标题: {page.driver.title}",
                            f"失败时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                        ]
                        allure.attach(
                            "\n".join(context_info),
                            name="失败上下文信息",
                            attachment_type=allure.attachment_type.TEXT
                        )

                        # 记录异常堆栈到日志
                        if hasattr(report, 'longrepr') and report.longrepr:
                            test_logger.error(f"异常详情:\n{report.longrepr}")

                except Exception as e:
                    test_logger.error(f"截图保存失败: {e}", exc_info=True)
        elif report.skipped:
            test_logger.warning(f" 测试跳过: {item.nodeid}")


# ==================== YamlFile 类 ====================
class YamlFile(pytest.File):
    def __init__(
            self,
            fspath: None = None,
            path_or_parent: Path | Node | None = None,
            path: Path | None = None,
            name: str | None = None,
            parent: Node | None = None,
            config: Config | None = None,
            session: Session | None = None,
            nodeid: str | None = None,
    ):
        super().__init__(fspath, path_or_parent, path, name, parent, config, session, nodeid)

        test_logger.info(f"初始化测试文件: {self.path}")

        """相当于setup_class"""
        try:
            service = Service(executable_path=r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])

            driver = webdriver.Chrome(service=service, options=options)
            driver.maximize_window()
            test_logger.info(" Chrome浏览器启动成功")

            self.page = BasePage(driver)
        except Exception as e:
            test_logger.error(f" 浏览器启动失败: {e}", exc_info=True)
            raise

    def teardown(self) -> None:
        test_logger.info(f"关闭浏览器: {self.path}")
        try:
            self.page.driver.quit()
            test_logger.info(" 浏览器已关闭")
        except Exception as e:
            test_logger.error(f"浏览器关闭失败: {e}")

    def collect(self) -> Iterable[Item | Collector]:
        with open(self.path, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
            test_logger.info(f" 加载YAML文件: {self.path}")
            test_logger.debug(f"YAML内容: {yaml_data}")

        base_data = yaml_data['base_data']
        test_cases = yaml_data['test_cases']

        test_logger.info(f"基础数据: {base_data.get('feature', 'Unknown')}")
        test_logger.info(f"测试用例数量: {len(test_cases)}")

        for idx, test_case in enumerate(test_cases):
            test_logger.info(f"生成测试项 [{idx + 1}/{len(test_cases)}]: {test_case.get('story', 'Unnamed')}")
            yield YamlItem.from_parent(
                self,
                name=test_case['story'],
                base_data=base_data,
                test_case=test_case,
                page=self.page,
                index=idx
            )


# ==================== YamlItem 类 ====================
class YamlItem(pytest.Item):
    def __init__(self, parent, name, base_data, test_case, page, index=0):
        super().__init__(name, parent)
        self.base_data = base_data
        self.test_case = test_case
        self.page: BasePage = page
        self.current_step_index = 0
        self.current_step_name = ""
        self.test_index = index
        self.step_results = []  # 记录每一步的执行结果

        test_logger.info(f"创建测试项: {name}")

    def setup(self) -> None:
        """相当于setup_method"""
        test_logger.info(f" 设置测试: {self.name}")
        test_logger.info(f"Feature: {self.base_data.get('feature', 'N/A')}")
        test_logger.info(f"Description: {self.base_data.get('description', 'N/A')}")

    def runtest(self) -> None:

        if not self.page:
            raise RuntimeError("Page对象未初始化，请确保通过夹具注入")

        # 打开对应页面
        target_url = TP_HOST + self.base_data['host']
        test_logger.info(f" 访问页面: {target_url}")
        self.page.driver.get(target_url)
        test_logger.info(f"页面标题: {self.page.driver.title}")

        allure.dynamic.feature(self.base_data['feature'])
        allure.dynamic.description(self.base_data['description'])
        allure.dynamic.story(self.test_case['story'])

        total_steps = len(self.test_case['steps'])
        test_logger.info(f" 开始执行测试步骤，共 {total_steps} 步")

        # 遍历测试步骤
        for index, step in enumerate(self.test_case['steps']):
            self.current_step_index = index
            self.current_step_name = step.get('step_name', f'步骤{index + 1}')

            test_logger.info(f"   执行步骤 [{index + 1}/{total_steps}]: {self.current_step_name}")
            test_logger.debug(f"    步骤详情: {step}")

            with allure.step(step['step_name']):
                try:
                    time.sleep(2)
                    event = self.page.__getattribute__(step['event'])
                    if event:
                        test_logger.debug(f"    调用方法: {step['event']}")
                        test_logger.debug(f"    参数: {step['arguments']}")

                        result = event(**step['arguments'])

                        if result is not None:
                            test_logger.debug(f"    返回结果: {result}")

                        if 'is_assert' in step.keys() and step['is_assert']:
                            test_logger.info(f"   断言验证: 期望={step['expect']}, 实际={result}")
                            assert step['expect'] == result
                            test_logger.info(f"   断言通过")
                        else:
                            test_logger.info(f"   步骤执行成功")

                        self.step_results.append({
                            'step': self.current_step_name,
                            'status': 'PASS',
                            'result': result
                        })
                    else:
                        error_msg = f"事件方法不存在: {step['event']}"
                        test_logger.error(error_msg)
                        raise AttributeError(error_msg)

                except AssertionError as e:
                    test_logger.error(f"   断言失败: 期望={step['expect']}, 实际={result}")
                    test_logger.error(f"   断言异常: {e}")
                    self.step_results.append({
                        'step': self.current_step_name,
                        'status': 'FAIL',
                        'error': str(e),
                        'expected': step.get('expect'),
                        'actual': result
                    })
                    raise

                except Exception as e:
                    test_logger.error(f"   步骤执行异常: {e}", exc_info=True)
                    self.step_results.append({
                        'step': self.current_step_name,
                        'status': 'ERROR',
                        'error': str(e)
                    })
                    raise

        # 记录所有步骤执行结果
        test_logger.info(f" 测试完成，总步骤: {total_steps}")
        success_count = sum(1 for r in self.step_results if r['status'] == 'PASS')
        test_logger.info(f"    成功: {success_count},  失败: {total_steps - success_count}")

        self.page.driver.delete_all_cookies()
        test_logger.info(f" Cookies已清除")