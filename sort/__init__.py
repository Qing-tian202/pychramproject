# __init__.py

from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort

# 定义公共API
__all__ = ['bubble_sort',
           'selection_sort',
           'insertion_sort',
           'merge_sort',
           'quick_sort']

# 版本信息
__version__ = '1.0.0'