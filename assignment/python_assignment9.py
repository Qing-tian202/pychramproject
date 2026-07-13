from typing import Optional
import random

class Person:
    __person_num = 0  # 类属性：记录创建的实例数

    def __init__(self, name: Optional[str] = "zhangsan", age: Optional[int] = 0) -> None:
        """
        构造函数，初始化实例属性
        :param name: 姓名
        :param age: 年龄
        """
        self.name = name    #实例属性：姓名
        if age < 0:
            raise ValueError("年龄不能为负数！")
        self.age = age      #实例属性：年龄

        self.__id = self.__set_id()  # 私有属性：ID，默认随机生成
        Person.__person_num += 1    # 每实例化一个对象，计数加一

    def get_name(self) -> str:
        """获取姓名"""
        return self.name

    def get_age(self) -> int:
        """获取年龄"""
        return self.age

    def set_name(self, name: str) -> None:
        """设置姓名"""
        self.name = name


    def set_age(self, age: int) -> None:
        """设置年龄(合法性校验)"""
        if age < 0:
            raise ValueError("年龄不能为负数！")
        self.age = age


    def __set_id(self):
        """
        私有方法，用于生成一个随机ID（演示用）
        实际中可使用uuid或数据库自增ID，这里简单返回随机数
        """
        # 为了演示，返回一个1-10000的随机整数，并转为字符串
        return str(random.randint(1, 10000))

    def get_id(self) -> int:
        """获取私有ID"""
        return self.__id

    @classmethod
    def get_person_num(cls) -> int:
        """获取当前创建实例数量"""
        return cls.__person_num

    @staticmethod
    def caculate_age(person1, person2) -> int:
        """
        计算两个人的年龄差（绝对值）
        :param person1: Person对象
        :param person2: Person对象
        :return: 年龄差的绝对值
        """
        if not isinstance(person1, Person) or not isinstance(person2, Person):
            raise TypeError("必须是Person对象！")
        return abs(person1.get_age() - person2.get_age())

    def __str__(self):
        return f"{self.name}({self.age})"


if __name__ == "__main__":
    # 1. 创建几个Person实例
    p1 = Person("张三", 25)
    p2 = Person("李四", 30)
    p3 = Person("王五", 28)

    # 2. 测试实例方法
    print("--- 实例方法测试 ---")
    print(f"p1 姓名: {p1.get_name()}, 年龄: {p1.get_age()}")
    p1.set_name("张伟")
    p1.set_age(26)
    print(f"修改后 p1: {p1}")

    # 3. 测试私有属性访问
    print(f"\n--- 私有属性测试 ---")
    print(f"p1 的ID (通过方法获取): {p1.get_id()}")
    # 下面这行会报错（私有属性无法直接访问），取消注释可看到错误
    # print(p1.__id)

    # 4. 测试类方法
    print(f"\n--- 类方法测试 ---")
    print(f"当前已创建 Person 实例数量: {Person.get_person_num()}")

    # 5. 测试静态方法
    print(f"\n--- 静态方法测试 ---")
    print(f"p1 和 p2 的年龄差: {Person.caculate_age(p1, p2)} 岁")
    print(f"p1 和 p3 的年龄差: {Person.caculate_age(p1, p3)} 岁")

    # 6. 额外演示：创建更多对象查看计数变化
    p4 = Person("赵六", 22)
    print(f"\n再创建 p4 后，实例总数: {Person.get_person_num()}")
