from typing import Optional
import random

id_pool = set()

class Student:
    """学生类：表示一个学生实体"""
    def __init__(self, logger, id: Optional[str] = None, name: Optional[str] = None, age: Optional[int] = None):
        """
        构造函数，初始化实例属性
        :param id: 编号
        :param name:  姓名
        :param age:  年龄
        """
        if not name:
            raise AttributeError("Student must have a name")
        self.__name = name

        if not id:
            raise AttributeError("Student must have a id!")
        self.__id = id

        if not age:
            raise AttributeError("Student must have age!")
        if age < 0 or age > 30:
            raise AttributeError("Student must have age between 0 and 30!")
        self.__age = age

    def __dict__(self):
        return f"'id':{self.id},'name':{self.name},'age':{self.age}"

    @property
    def id(self):
        """访问 id"""
        return self.__id

    @property
    def name(self):
        """访问 姓名"""
        return self.__name

    @name.setter
    def name(self, name: Optional[str] = None):
        """修改 姓名"""
        if name is None:
            raise AttributeError("Student must have a name")

        self.__name = name

    @property
    def age(self):
        """访问 年龄"""
        return self.__age

    @age.setter
    def age(self, age: Optional[int] = None):
        if not age:
            raise AttributeError("Student must have a score!")
        if age < 0 or age > 30:
            raise AttributeError("Student must have a age between 0 and 30!")
        self.__age = age

    @staticmethod
    def generate_id():
        """静态方法，生成唯一的学生id"""
        while True:
            new_id = str(random.randint(10000, 99999))
            if new_id not in id_pool:
                id_pool.add(new_id)
                return new_id