import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
import traceback
from typing import Iterable
from .Logger import setup_logging


class DBTool:

    logger = setup_logging()

    @classmethod
    def __init__(cls, host = "192.168.44.130", user = "root", password = "123456", database = "shool",port = 3306):
        """
        创建数据库连接
        :param host: 主机地址
        :param user: 用户名
        :param password: 密码
        :param database: 数据库
        :param port: 端口
        :return: 数据库连接指针
        """
        try:
            cls.host = host
            cls.user = user
            cls.password = password
            cls.database = database
            cls.port = port

            conn = mysql.connector.connect(host = host, user = user, password = password, database = database, port = port)
            cls.logger.info("连接数据库成功！")
            return conn
        except Exception as e:
            #pass
            cls.logger.error(f"连接数据库失败：{e} \n  {traceback.format_exc()}")


    @classmethod
    def query_data(cls,query:str,args:object | None = None ,id: int = 0):
        """
        查询数据库数据
        执行查询语句并返回结果

        :param sql: SQL查询字符串
        :param args: 查询参数（单个值或元组/字典）
        :param id: 0 = 获取所有结果, n>0 = 获取指定ID的结果
        :return: 查询结果集
        """
        conn = None
        cursor = None
        try:
            conn = cls.__init__()  # 初始化数据库连接
            cursor = conn.cursor()  # 创建游标对象

            # 执行查询并获取影响行数
            affected_rows = cursor.execute(query, args)
            # 记录执行日志
            cls.logger.info(f"SQL：{query},args: {args}, affected_rows：{affected_rows}")

            # 根据fetcha_number返回相应数量的结果
            if id == 0:
                return cursor.fetchall()  # 获取所有结果
            else:
                return cursor.fetchone()  # 获取指定数量的结果

        except Exception as e:
            #pass
            # 异常处理：记录错误日志
            cls.logger.error(f"SQL：{query},args: {args}\n \t{e}")
        finally:
            # 资源清理：确保关闭游标和连接
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            cls.logger.info("查询操作结束，关闭数据库连接！")

    @classmethod
    def update_table(cls, query, args: Iterable[object], execute_many: bool = False):
        """
        执行数据变更操作（INSERT/UPDATE/DELETE）
        :param query:SQL查询字符串
        :param args: 参数集合（可迭代对象）
        :param execute_many:
                        False - 将args整体作为单次执行参数;
                        True - 遍历args，多次执行相同SQL语句
        :return:
        """
        my_conn = None
        my_cursor = None

        try:
            my_conn = cls.__init__()  # 初始化数据库连接
            my_cursor = my_conn.cursor()  # 创建游标对象

            if execute_many:
                # 循环执行模式：遍历参数集合逐条执行
                for arg in args:
                    my_cursor.execute(query, arg)
            else:
                # 单次执行模式：使用整个参数集合
                my_cursor.execute(query, args)

            # 打印受影响的行数（调试用）
            #print(f"Affected rows:", my_cursor.rowcount)
            if my_cursor.rowcount == 0:
                raise

            # 提交事务（必须的DML操作步骤）
            my_conn.commit()

            # 记录成功日志
            cls.logger.info(f"SQL：{query},args: {args}，\n \t影响行数：{my_cursor.rowcount}")

        except Exception as e:
            # 异常处理：回滚事务并记录错误
            if my_conn:
                my_conn.rollback()
            cls.logger.error(f"SQL：{query},args: {args}\n \t执行DML语句执行失败：{e}")
        finally:
            # 资源清理：确保关闭游标和连接
            if my_cursor:
                my_cursor.close()
            if my_conn:
                my_conn.close()
            cls.logger.info("更新数据库完成，关闭数据库连接！")


# if __name__ == '__main__':
#     sql = "select * from student6 where id = %s"
#     args = (2,)
#     print(DBTool.query_data(sql,args,2))