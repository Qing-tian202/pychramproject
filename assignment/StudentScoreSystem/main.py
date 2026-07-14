import json
import logging
import os
from datetime import datetime
import traceback


def setup_logging():
    """配置日志系统"""
    # 创建日志目录
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 生成日志文件名（按日期）
    log_file = os.path.join(log_dir, f"student_system_{datetime.now().strftime('%Y%m%d')}.log")

    # 配置日志格式
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    # 配置日志记录器
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),  # 写入文件
            #logging.StreamHandler()  # 同时输出到控制台
        ]
    )

    return logging.getLogger(__name__)

def data_input(logger):
    """数据输入"""
    try:
        name = input("请输入学生姓名：")
        subject = input("请输入学科：")
        if not name or not subject:
            raise ValueError("姓名或学科不能为空！")
        logger.info(f"获取用户输入：姓名 = '{name}', 学科 = '{subject}'")
        return name, subject
    except ValueError as e:
        logger.error(f"输入验证失败： {e}")


def add_student(df,logger):
    """添加学生"""
    try:
        logger.info(f"开始执行添加学生操作：")

        new_name , new_subject = data_input(logger)
        new_score =  int(input("请输入分数："))

        if new_score <= 0 or new_score > 100:
            raise ValueError("请输入正确的分数！")

        new_student = {
            "name": new_name,
            "subject": new_subject,
            "score": new_score
        }
        df.append(new_student)
        logger.info(f"添加学生成功： 姓名 = '{new_name}' , 学科 = '{new_subject}' , 成绩 = '{new_score}'")
        return df
    except ValueError as e:
        logger.error(f"添加学生失败：{e}")
    except Exception as e:
        logger.error(f"添加过程中发生未知错误：{e} \n {traceback.format_exc()}")

def update_student(df,logger):
    """更新学生成绩"""
    try:
        logger.info(f"开始执行更新学生成绩操作：")
        student_name, student_subject = data_input(logger)
        score = int(input("请输入修改后的分数："))

        if score <= 0 or score > 100:
            raise ValueError("请输入正确的分数！")

        found = False
        for item in df:
            if item.get("name") == student_name and item.get("subject") == student_subject:
                old_score = item.get("score")
                item["score"] = score
                found = True
                logger.info(f"更新学生成绩成功：姓名 = '{student_name}' , 学科 = '{student_subject}'"
                            f"旧成绩 = '{old_score}' , 新成绩 = '{score}'")
                break

        if not found:
            logger.warning(f"未找到需要更新的学生：姓名 = '{student_name}' , 学科 = '{student_subject}'")
        return df,found
    except ValueError as e:
        logger.error(f"更新学生成绩失败： {e}")
    except Exception as e:
        logger.error(f"更新过程发生未知错误: {e} \n {traceback.format_exc()}")


def delete_student(df,logger):
    """删除指定学生"""
    try:
        logger.info(f"开始执行删除学生操作：")
        student_name, student_subject = data_input(logger)

        found = False
        for item in df:
            if item.get("name") == student_name and item.get("subject") == student_subject:
                found = True
                df.remove(item)
                logger.info(f"删除学生成功： 姓名 = '{student_name}' , 成绩 = '{student_subject}'")
                break

        if not found:
            logger.warning(f"未找到需要删除的学生：姓名 = '{student_name}' , 学科 = '{student_subject}'")
        return df,found

    except Exception as e:
        logger.error(f"删除学生过程发生未知错误: {e} \n {traceback.format_exc()}")

def search_student(df,logger):
    """查找指定学生"""
    try:
        logger.info(f"开始执行查找学生操作")
        student_name, student_subject = data_input(logger)

        for item in df:
            if item.get("name") == student_name and item.get("subject") == student_subject:
                logger.info(f"查找学生成功：姓名 = '{student_name}' , 学科 = '{student_subject}'")
                return item
        logger.warning(f"未找到需要删除的学生：姓名 = '{student_name}' , 学科 = '{student_subject}'")
        return None
    except Exception as e:
        logger.error(f"查找学生过程发生未知错误: {e} \n {traceback.format_exc()}")

def pprint(df,logger):
    """打印所有学生信息"""
    try:
        logger.info(f"开始执行打印所有学生信息操作")
        if not df:
            logger.info(f"")
        print("所有学生信息，如下表：")
        print(f"{'姓名':<10} {'学科':<10} {'成绩':<10}")
        for item in df:
            print(f"{item.get('name'):<10} {item.get('subject'):<10} {item.get('score'):<10}")

def show_menu():
    # 打印菜单栏
    print("----------------学生成绩管理系统----------------")
    print("""
                    1.新增学生信息:(i/insert)
                    2.删除学生信息:(d)
                    3.修改学生信息:(u)
                    4.查找单个学生信息:(q)
                    5.打印菜单:(p)
                    6.打印所有学生信息(qa)
                    0.退出系统:(quit)
                """)

def menu(df):
    show_menu()
    while True:

        op = input("请输入你的操作:")
        if op in ["quit", "0"]:
            return df
        elif op in ["i", "insert", "1"]:
            df = add_student(df,logger)
        elif op in ["q", "4"]:
            student = search_student(df,logger)
            if student:
                print(f"学生姓名：{student.get('name')} 科目：{student.get('subject')} 成绩：{student.get('score')}")
            else:
                print(f"没有该学生！")
        elif op in ["d", "2"]:
            df = delete_student(df,logger)
        elif op in ["u", "3"]:
            df = update_student(df,logger)
        elif op in ["p", "5"]:
            show_menu()
        elif op in ["qa", "6"]:
            pprint(df,logger)
        else:
            continue


def main(logger):
    try:
        file_name = "data.json"
        if not os.path.exists(file_name):
            raise FileExistsError("文件不存在")

        df = []

        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)
            df = data.get("students")

        # print(df)
        df = menu(df,logger)
        # print(df)
        if df:
            data = {"students": df}
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    except FileExistsError as e:
        print(f"错误：{e}")

    except ValueError as e:
        print(f"请输入正确的数据： {e}")

    except Exception as e:
        print(f"未知错误： {e}")

if __name__ == '__main__':
    # 初始化日志
    logger = setup_logging()

    #开始执行
    main(logger)



