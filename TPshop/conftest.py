import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from abc import ABC
from pathlib import Path
from typing import Iterable

import _pytest.hookspec
import allure
import pytest
import yaml
from _pytest.config import Config
from _pytest.main import Session
from _pytest.nodes import Collector, Item, Node
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from common import BasePage
from tools import TP_HOST


def pytest_collect_file(file_path: Path, parent: Collector) -> Collector | None:
    # print(file_path.parent.name)
    # 把data目录下的所有yaml文件视作测试文件
    if file_path.suffix == '.yaml' and file_path.parent.name == 'data':
        return YamlFile.from_parent(parent=parent, path=file_path)


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

        """相当于setup_class"""
        service = Service(executable_path=r"D:\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        self.page = BasePage(driver)

    def teardown(self) -> None:
        self.page.driver.quit()

    def collect(self) -> Iterable[Item | Collector]:
        with open(self.path, encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)

        base_data = yaml_data['base_data']
        test_cases = yaml_data['test_cases']

        for test_case in test_cases:
            yield YamlItem.from_parent(self, name=test_case['story'],
                                       base_data=base_data,
                                       test_case=test_case,
                                       page=self.page)


class YamlItem(pytest.Item):
    def __init__(self, parent, name, base_data, test_case,page):
        super().__init__(name, parent, )
        self.base_data = base_data
        self.test_case = test_case
        self.page: BasePage = page

    def setup(self) -> None:
        """相当于setup_method"""
        pass

    def runtest(self) -> None:
        # 打开对应页面
        self.page.driver.get(TP_HOST + self.base_data['host'])

        allure.dynamic.feature(self.base_data['feature'])
        allure.dynamic.description(self.base_data['description'])
        allure.dynamic.story(self.test_case['story'])

        # 遍历测试步骤
        for step in self.test_case['steps']:
            with allure.step(step['step_name']):
                time.sleep(2)
                event = self.page.__getattribute__(step['event'])
                if event:
                    result = event(**step['arguments'])

                    if 'is_assert' in step.keys():
                        if step['is_assert']:
                            assert step['expect'] == result

        self.page.driver.delete_all_cookies()