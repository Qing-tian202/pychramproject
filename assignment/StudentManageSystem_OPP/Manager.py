import traceback
from typing import Optional
from Student import Student
import os
import json

class Manager:
    """管理员类，负责学生数据的增删改查等操作"""
    def __init__(self, logger , file_name: Optional[str] = 'data.json'):
        """
        构造函数，实例化对象
        :param logger: 日志记录器
        :param file_name: 数据存放文件名
        """
        self.file_name = file_name
        self.students = []  #存储学生对象
        self.logger = logger #日志

    def load_data(self):
        """载入数据"""
        try:
            self.logger.info(f"开始载入数据")
            if not os.path.exists(self.file_name):
                raise FileNotFoundError(f"文件不存在：{self.file_name}")

            with open(self.file_name, "r", encoding='utf-8') as f:
                data = json.load(f)

                for item in data:
                    student = Student(
                        self.logger,
                        item.get("id"),
                        item.get("name"),
                        item.get("age")
                    )
                    self.students.append(student)
            self.logger.info(f"载入数据成功：{self.students}")
        except FileNotFoundError as e:
            self.logger.error(f"载入数据失败：{e}")
        except json.JSONDecodeError:
            self.logger.error(f"载入数据失败, 文件 {self.file_name} 格式错误，将重新创建")
            self.save_data(False)
        except Exception as e:
            self.logger.error(f"载入数据发生错误：{e} \n {traceback.format_exc()}")

    def save_data(self, flage: Optional[bool] = True):
        """
        保存数据
        :param flage: 是否需要创建新文件，默认不需要
        :return:
        """
        if flage:
            try:
                self.logger.info(f"开始保存数据")
                if self.students:
                    with open(self.file_name, "w",encoding='utf-8') as f:
                        data = [student.dict() for student in self.students]
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        self.logger.info(f"保存数据成功：{data}")

                else:
                    self.logger.warning(f"没有数据需要保存")
            except Exception as e:
                self.logger.error(f"保存数据发生错误：{e} \n {traceback.format_exc()}")

        else:
            try:
                self.logger.info(f"开始创建新文件")
                with open(self.file_name, "w",encoding='utf-8') as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                self.logger.info(f"创建文件成功")
            except Exception as e:
                self.logger.error(f"创建文件失败：{e} \n {traceback.format_exc()}")


    def add_student_data(self, n: Optional[int] = 0, index: Optional[int] = 0):
        """
        添加操作
        :param n: 插入条数(0 表示使用默认数据)
        :param index: 最大的编号（可选）
        :return: 修改后的数据列表
        """
        if not n:
            student = Student(self.logger, Student.generate_id(self.logger),"zhangsan",20)
        else:
            for i in range(n):
                name = input(f"请输入第{i + 1}个学生的名字:")
                age = int(input(f"请输入第{i + 1}个学生的年龄:"))
                student = Student(self.logger,i + 1 + index, name, age)
                self.students.append(student)
                self.logger.info(f"成功添加第{i + 1}条学生信息："
                                 f"id={student.id} name={student.name} age={student.age}")


    def insert_student(self):
        """添加学生信息"""
        try:
            self.logger.info(f"开始添加学生信息")
            n = int(input("您要新增几条数据，请输入:"))

            if not self.students:
                self.add_student_data(n)
            else:
                self.students.sort(key = lambda student:student.id )
                last_id = self.students[-1].id
                self.add_student_data(n, last_id)

            self.logger.info(f"成功新增 {n} 条学生信息！")
            return self.students
        except Exception as e:
            self.logger.error(f"添加学生信息过程发生错误: {e} \n {traceback.format_exc()}")

    def query_student(self, id: Optional[int] = 0):
        """
        查询操作
        :param id: id（可选，默认查询全部数据）
        :return:
        """
        try:
            if not id:
                self.logger.info(f"开始查询所有学生信息")

                if not self.students:
                    self.logger.warning(f"系统数据为空")

                else:
                    self.logger.info("已查到所有学生信息，如下表：")
                    self.logger.info(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")
                    print("已查到所有学生信息，如下表：")
                    print(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")

                    for student in self.students:
                        print(f"{student.id:<6} {student.name:<10} {student.age}")
                        self.logger.info(f"{student.id:<6} {student.name:<10} {student.age:<4}")

            else:
                self.logger.info(f"开始查询 id = {id} 的学生")
                if not self.students:
                    self.logger.warning(f"系统数据为空")
                    self.logger.info(f"对不起，学生编号为【{id}】的学生不存在！")
                    print(f"对不起，学生编号为【{id}】的学生不存在！")

                else:
                    for student in self.students:
                        if student.id == id:
                            print(f"{student.id:<6} {student.name:<10} {student.age}")
                            self.logger.info(f"成功查询到一条消息： {student.id:<6} {student.name:<10} {student.age:<4}")
                            return student

                    self.logger.info(f"对不起，学生编号为【{id}】的学生不存在！")
                    print(f"对不起，学生编号为【{id}】的学生不存在！")

        except Exception as e:
            self.logger.error(f"查询过程出现错误: {e} \n {traceback.format_exc()}")

    def delete_student(self, id: Optional[str] = None):
        """
        删除学生信息
        :param id: 学生id（id为0表示删除所有数据），可选，默认删除所有数据
        :return: 修改后的数据列表
        """
        try:
            if not id:
                    self.logger.info(f"开始删除全部数据")
                    self.students = []
                    self.logger.info(f"删除数据{len(self.students)}条")
                    return self.students
            else:
                self.logger.info(f"开始删除指定学生")

                student = self.query_student(int(id))
                if not student:
                    self.logger.error(f"删除失败：未找到欲删除id: {id}的学生")
                    return self.students
                self.students.remove(student)
                self.logger.info(f"成功删除一条数据：{student.id:<6} {student.name:<10} {student.age:<4}")
                return self.students

        except Exception as e:
            self.logger.error(f"删除过程出现错误: {e} \n {traceback.format_exc()}")


    def update_student(self, id, *args):
        """
        更新学生信息
        :param id: id
        :param args: 要更新的数据：姓名、年龄、姓名和年龄
        :return: 修改后的数据列表
        """
        try:
            self.logger.info(f"开始更新学生信息")
            if not self.students:
                self.logger.error(f"数据列表为空，更新失败")
                return self.students
            else:
                student = self.query_student(id)
                if not student:
                    self.logger.error(f"更新失败：未找到 id:{id} 的学生")

                old_name, old_age = student.name, student.age
                if len(args) == 2:
                    name, age = args
                    student.name , student.age = name, age
                    self.logger.info(f"成功更新一条数据，旧数据 {student.id:<6} {old_name:<10} {old_age:<4}"
                                     f"新数据 {student.id:<6} {student.name:<10} {student.age:<4}")
                    return self.students
                else:
                    if args[0].isdigit():
                        student.age = int(args[0])
                        self.logger.info(f"成功更新一条数据，旧数据 {student.id:<6} {old_name:<10} {old_age:<4}"
                                         f"新数据 {student.id:<6} {student.name:<10} {student.age:<4}")
                        return self.students
                    else:
                        student.name = args[0]
                        self.logger.info(f"成功更新一条数据，旧数据 {student.id:<6} {old_name:<10} {old_age:<4}"
                                         f"新数据 {student.id:<6} {student.name:<10} {student.age:<4}")
                        return self.students
        except Exception as e:
            self.logger.error(f"更新过程出现错误: {e} \n {traceback.format_exc()}")

    def count_students(self):
        """统计数据条数"""
        try:
            self.logger.info(f"开始统计数据条数")
            return len(self.students)
        except Exception as e:
            self.logger.error(f"统计过程出现错误: {e} \n {traceback.format_exc()}")


    def run(self):
        """运行系统"""
        self.logger.info(f"欢迎使用本系统！")
        self.load_data()
        Manager.show_menu()
        while True:
            try:
                op = input("请输入您的操作:")
                if op in ["quit", "0"]:
                    self.logger.info(f"感谢使用本系统，再见！")
                    return self.save_data() #退出系统，保存数据
                elif op in ["i", "insert", "1"]:
                    self.students = self.insert_student()
                    self.save_data() #每次更改后保存数据放丢失
                elif op in ["q", "qa", "4", "5"]:
                    if op in ["q", "4"]:
                        id = int(input("请输入您要查询的学生编号(0代表所有学生)："))

                        if id < 0: #合法性验证
                            raise ValueError("请输入正确的id")
                        self.query_student(id)
                    else:
                        self.query_student(0)
                elif op in ["d", "da", "2", "6"]:
                    if op in ["d", "2"]:
                        id = int(input("请输入您要删除的学生编号(0代表所有学生)："))

                        if id < 0: #合法性验证
                            raise ValueError("请输入正确的id")

                        self.students = self.delete_student()
                    else:
                        self.students = self.delete_student(0)

                    self.save_data() #每次更改后保存数据放丢失
                elif op in ["u", "3"]:
                    id = int(input("请输入您要修改的学生编号："))

                    if id < 0:  # 合法性验证
                        raise ValueError("请输入正确的id")

                    modify_info = input("请输入新的数据(格式: 姓名 年龄)，若没有则输入:").split()
                    self.students = self.update_student(id, modify_info)
                    self.save_data() #每次更改后保存数据放丢失

                elif op in ["c", " 7"]:
                    n = self.count_students()
                    self.logger.info(f"成功统计到{n}条数据")

                elif op in ["p", "8"]:
                    self.logger.info(f"开始打印菜单")
                    Manager.show_menu()
                    self.logger.info(f"成功打印菜单")
                else:
                    self.logger.error(f"无效操作: {op} \n {traceback.format_exc()}")
                    continue
            except ValueError as e:
                self.logger.error(f"验证失败：{e}")
            except Exception as e:
                self.logger.error(f"运行出错: {e} \n {traceback.format_exc()}")

    @staticmethod
    def show_menu():
        """打印菜单栏"""
        print("----------------重软学院学生管理系统----------------")
        print("""
                1.新增学生信息:(i/insert)
                2.删除学生信息:(d)
                3.修改学生信息:(u)
                4.查找单个学生信息:(q)
                5.查找所有学生信息:(qa)
                6.清空学生系统:(da)
                7.统计学生总数:(c)
                8.打印菜单:(p)
                0.退出系统:(quit)
            """)


