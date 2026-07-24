# test_add.py - 测试用例
import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import allure
from typing import Optional
from common.build_add_data import build_add_data
from common.build_multy_data import build_multy_data


def add(x: Optional[float] = 0, y: Optional[float] = 0) -> float:
    """加法函数"""
    result = round(x + y, 2)
    return result


def multy(x: Optional[float] = 1, y: Optional[float] = 1) -> float:
    """乘法函数"""
    result = round(x * y, 2)
    return result


@allure.epic("数学运算测试")
@allure.feature("加法运算")
class TestAddFunc:
    """加法函数测试类"""

    @allure.story("基础加法测试")
    @allure.title("测试加法功能 - {x} + {y} = {expected}")
    @pytest.mark.parametrize("x, y, expected", build_add_data())
    def test_add(self, x, y, expected):
        """测试加法函数"""
        with allure.step(f"执行加法: {x} + {y}"):
            result = add(x, y)

        with allure.step(f"验证结果: 期望 {expected}，实际 {result}"):
            assert result == expected, f"add({x}, {y}) = {result}，期望 {expected}"

        allure.attach(
            f"输入: x={x}, y={y}",
            name="输入参数",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            f"输出: {result}",
            name="输出结果",
            attachment_type=allure.attachment_type.TEXT
        )


@allure.epic("数学运算测试")
@allure.feature("乘法运算")
class TestMultyFunc:
    """乘法函数测试类"""

    @allure.story("基础乘法测试")
    @allure.title("测试乘法功能 - {x} × {y} = {expected}")
    @pytest.mark.parametrize("x, y, expected", build_multy_data())
    def test_multy(self, x, y, expected):
        """测试乘法函数"""
        with allure.step(f"执行乘法: {x} × {y}"):
            result = multy(x, y)

        with allure.step(f"验证结果: 期望 {expected}，实际 {result}"):
            assert result == expected, f"multy({x}, {y}) = {result}，期望 {expected}"

        allure.attach(
            f"输入: x={x}, y={y}",
            name="输入参数",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            f"输出: {result}",
            name="输出结果",
            attachment_type=allure.attachment_type.TEXT
        )