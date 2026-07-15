from typing import Optional
import random
import traceback

id_pool = set()

class Student:
    """学生类：表示一个学生实体"""
    def __init__(self, logger, id: Optional[int] = 0, name: Optional[str] = None, age: Optional[int] = None):
        """
        构造函数，初始化实例属性
        :param logger: 日志记录器
        :param id: 编号
        :param name:  姓名
        :param age:  年龄
        """
        try:
            self.logger = logger
            self.logger.info(f"开始实例化对象")
            if not name:
                raise AttributeError("学生必须有姓名 ！")
            self.__name = name

            if not id:
                raise AttributeError("学生必须有 id!")
            self.__id = id

            if not age:
                raise AttributeError("学生必须有年龄!")
            if age < 0 or age > 30:
                raise AttributeError("学生年龄必须在0-30之间!")
            self.__age = age
            self.logger.info(f"实例化对象 id = {self.__id}, name = {self.__name}, "
                             f"age = {self.__age} 成功！")
        except AttributeError as e:
            self.logger.error(f"实例化对象失败：{e}")
        except Exception as e:
            self.logger.error(f"实例化过程未知错误: {e} \n {traceback.format_exc()}")


    def dict(self):
        self.logger.info(f"开始执行转换为字典操作")
        s = {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }
        self.logger.info(f"转换成功：{s}")
        return s

    @property
    def id(self):
        """访问 id"""
        return self.__id

    @id.setter
    def id(self, new_id: Optional[int] = None):
        if not new_id:
            self.__id = Student.generate_id(logger=self.logger)
        else:
            self.__id = new_id

    @property
    def name(self):
        """访问 姓名"""
        return self.__name

    @name.setter
    def name(self, name: Optional[str] = None):
        """修改 姓名"""
        try:
            self.logger.info(f"开始执行更新姓名操作")
            if name is None:
                raise AttributeError("学生必须有姓名！")

            self.__name = name
            self.logger.info(f"更新姓名成功！")
        except AttributeError as e:
            self.logger.error(f"姓名更新失败: {e}")
        except Exception as e:
            self.logger.error(f"更新姓名过程出现未知错误: {e} \n {traceback.format_exc()}")

    @property
    def age(self):
        """访问 年龄"""
        return self.__age

    @age.setter
    def age(self, age: Optional[int] = None):
        """设置 年龄"""
        try:
            self.logger.info(f"开始执行更新年龄操作")
            if not age:
                raise AttributeError("学生必须有年龄!")
            if age < 0 or age > 30:
                raise AttributeError("学生年龄必须在0-30之间!")
            self.__age = age
            self.logger.info(f"年龄更新成功")
        except AttributeError as e:
            self.logger.error(f"年龄更新失败: {e}")
        except Exception as e:
            self.logger.error(f"更新年龄过程出现未知错误: {e} \n {traceback.format_exc()}")

    @staticmethod
    def generate_id(logger):
        """静态方法，生成唯一的学生id"""
        logger.info(f"开始生成 id(唯一)")
        while True:
            new_id = random.randint(10000, 99999)
            if new_id not in id_pool:
                id_pool.add(new_id)
                logger.info(f"成功生成id：{new_id}")
                return new_id