from typing import Optional
from Student import Student
import os
import json

class Manager:
    """管理员类，负责学生数据的增删改查等操作"""
    def __init__(self, logger , file_name: Optional[str] = 'data.json'):
        """
        构造函数，实例化对象
        :param file_name: 文件名
        """
        self.file_name = file_name
        self.students = []  #存储学生对象
        self.logger = logger #日志
        self.load_data()

    def load_data(self):
        """载入数据"""
        if not os.path.exists(self.file_name):
            raise FileNotFoundError(f"文件不存在：{self.file_name}")

        try:
            with open(self.file_name, "r", encoding='utf-8') as f:
                data = json.load(f)
                print(data)
                for item in data:
                    student = Student(
                        self.logger,
                        item.get("id"),
                        item.get("name"),
                        item.get("age")
                    )
                    self.students.append(student)
        except json.JSONDecodeError:
            print(f"文件 {self.file_name} 格式错误，将重新创建")
            self.save_data()

    def save_data(self):
        """保存数据"""
        if self.students:
            with open(self.file_name, "w",encoding='utf-8') as f:
                for student in self.students:
                    json.dump(dict(student), f, ensure_ascii=False, indent=4)



    def insert_student(self):
        """添加学生信息"""
        n = int(input("您要新增几条数据，请输入:"))

        if not self.students:
            for i in range(n):
                name = input(f"请输入第{i + 1}个学生的名字:")
                age = input(f"请输入第{i + 1}个学生的年龄:")
                student = Student(i + 1, name, age)
                self.students.append(student)
        else:
            last_id = self.students[-1].id
            for i in range(n):
                name = input(f"请输入第{i + 1}个学生的名字:")
                age = input(f"请输入第{i + 1}个学生的年龄:")
                student = Student(last_id + i + 1, name, age)
                self.students.append(student)

        print(f"成功新增 {n} 条学生信息！")
        return self.students
