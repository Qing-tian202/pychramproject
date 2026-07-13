# __init__.py

from .connect import connect
from .close import close
from .insert import insert
from .update import update
from .query import query
from .delete import delete
from .count import count

# 公共接口
__all__ = ['connect',
           'close',
           'insert',
           'update',
           'query',
           'delete',
           'count']


__version__ = '1.0.0'