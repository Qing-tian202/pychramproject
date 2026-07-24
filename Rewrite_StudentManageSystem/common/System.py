import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.Logger import setup_logging
from tools.DBTool import DBTool
import traceback

class System:
    def __init__(self):
        self.logger = setup_logging()

    def insert_student(self):
        """插入学生数据"""
        sql = "insert into student6 (name,age) values(%s,%s)"
        data = []
        try:
            self.logger.info(f"开始添加学生信息")
            n = int(input("您要新增几条数据，请输入:"))

            for i in range(n):
                name = input(f"请输入第{i + 1}个学生的名字:")
                age = int(input(f"请输入第{i + 1}个学生的年龄:"))
                data.append((name, age))
            DBTool.update_table(sql, data,execute_many=True)

            self.logger.info(f"成功新增 {n} 条学生信息！")
        except Exception as e:
            self.logger.error(f"添加学生信息过程发生错误: {e} \n {traceback.format_exc()}")

    def delete_student(self, id = 0):
        """
        删除学生信息
        :param id: 学生id（id为0表示删除所有数据），可选，默认删除所有数据
        """
        try:
            if not id:
                self.logger.info(f"开始删除全部数据")
                self.logger.info(f"删除数据{self.count_student()}条")
                DBTool.update_table("DELETE FROM students",[])
                DBTool.update_table("ALTER TABLE students AUTO_INCREMENT = 1", [])

            else:
                self.logger.info(f"开始删除指定学生")

                student = DBTool.query_data("select * from student6 where id = %s",(id,))
                if not student:
                    self.logger.error(f"删除失败：未找到欲删除id: {id}的学生")

                DBTool.update_table("DELETE FROM student6 WHERE id = %s",(id,))
                self.logger.info(f"成功删除一条数据：{student[0]:<6} {student[1]:<10} {student[3]:<4}")

        except Exception as e:
            self.logger.error(f"删除过程出现错误: {e} \n {traceback.format_exc()}")

    def update_student(self,id,*args):
        """
        更新学生信息
        :param id: id
        :param args: 要更新的数据：姓名、年龄、姓名和年龄
        """
        try:
            self.logger.info(f"开始更新学生信息")
            sql = "select * from student6 "
            res = DBTool.query_data(sql, id=0)

            if not res:
                self.logger.error(f"数据列表为空，更新失败")
            else:
                student = self.query_student(id)
                if not student:
                    self.logger.error(f"更新失败：未找到 id:{id} 的学生")

                old_name, old_age = student[1], student[3]
                if len(args) == 2:
                    name, age = args
                    DBTool.update_table("update students set name = %s, age = %s where id = %s",(name, age, id))
                    self.logger.info(f"成功更新一条数据，旧数据 {id:<6} {old_name:<10} {old_age:<4}"
                                     f"新数据 {id:<6} {name:<10} {age:<4}")
                else:
                    if args[0].isdigit():
                        DBTool.update_table("update students set age = %s where id = %s",(int(args[0]), id))
                        self.logger.info(f"成功更新一条数据，旧数据 {id:<6} {old_name:<10} {old_age:<4}"
                                         f"新数据 {id:<6} {old_name:<10} {int(args[0]):<4}")

                    else:
                        DBTool.update_table("update students set set name = %s where id = %s",(args[0], id))
                        self.logger.info(f"成功更新一条数据，旧数据 {id:<6} {old_name:<10} {old_age:<4}"
                                         f"新数据 {id:<6} {old_name:<10} {int(args[0]):<4}")

        except Exception as e:
            self.logger.error(f"更新过程出现错误: {e} \n {traceback.format_exc()}")

    def query_student(self,id=0):
        """
        根据指定ID查询学生
        :param id: id（可选，默认查询全部数据）
        """
        try:
            if not id:
                self.logger.info(f"开始查询所有学生信息")
                sql = "select * from student6 "
                res = DBTool.query_data(sql, id=0)

                if not res:
                    self.logger.warning(f"系统数据为空")
                else:
                    self.pprint_student(res)

            else:
                self.logger.info(f"开始查询 id = {id} 的学生")
                sql = "select * from student6 where id = %s"
                res = DBTool.query_data(sql,(id,), id=id)
                if not res:
                    self.logger.warning(f"系统数据为空")
                    self.logger.info(f"对不起，学生编号为【{id}】的学生不存在！")
                    print(f"对不起，学生编号为【{id}】的学生不存在！")

                else:
                    self.pprint_student(res)

        except Exception as e:
            self.logger.error(f"查询过程出现错误: {e} \n {traceback.format_exc()}")

    def count_student(self):
        n = len(DBTool.query_data("select * from student6",id=0))
        return n

    def pprint_student(self,student_list):
        """打印查询到的学生信息"""
        self.logger.info("已查到所有学生信息，如下表：")
        self.logger.info(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")
        print("已查到所有学生信息，如下表：")
        print(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")

        for id,name,_,age in student_list:
            print(f"{id:<6} {name:<10} {age}")
            self.logger.info(f"{id:<6} {name:<10} {age:<4}")


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

    def run(self):
        """运行系统"""
        self.logger.info(f"欢迎使用本系统！")
        System.show_menu()
        while True:
            try:
                op = input("请输入您的操作:")
                if op in ["quit", "0"]:
                    self.logger.info(f"感谢使用本系统，再见！")
                    return
                elif op in ["i", "insert", "1"]:
                    self.insert_student()

                elif op in ["q", "qa", "4", "5"]:
                    if op in ["q", "4"]:
                        id = int(input("请输入您要查询的学生编号(0代表所有学生)："))

                        if id < 0:  # 合法性验证
                            raise ValueError("请输入正确的id")
                        self.query_student(id)
                    else:
                        self.query_student()
                elif op in ["d", "da", "2", "6"]:
                    if op in ["d", "2"]:
                        id = int(input("请输入您要删除的学生编号(0代表所有学生)："))

                        if id < 0:  # 合法性验证
                            raise ValueError("请输入正确的id")

                        self.delete_student(id)
                    else:
                        self.delete_student()

                elif op in ["u", "3"]:
                    id = int(input("请输入您要修改的学生编号："))

                    if id < 0:  # 合法性验证
                        raise ValueError("请输入正确的id")

                    modify_info = input("请输入新的数据(格式: 姓名 年龄)，若没有则输入:").split()
                    self.update_student(id, modify_info)

                elif op in ["c", " 7"]:
                    n = self.count_student()
                    print(f"学生数据 {n} 条")
                    self.logger.info(f"成功统计到{n}条数据")

                elif op in ["p", "8"]:
                    self.logger.info(f"开始打印菜单")
                    System.show_menu()
                    self.logger.info(f"成功打印菜单")
                else:
                    self.logger.error(f"无效操作: {op} \n {traceback.format_exc()}")
                    continue
            except ValueError as e:
                self.logger.error(f"验证失败：{e}")
            except Exception as e:
                self.logger.error(f"运行出错: {e} \n {traceback.format_exc()}")