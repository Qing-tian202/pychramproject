import Database

def insert(db):
    """
    :param db: 数据库指针db
    :return: 数据库指针db
    """
    n = int(input("您要新增几条数据，请输入:"))
    for i in range(n):
        name = input(f"请输入第{i+1}个学生的名字:")
        age = int(input(f"请输入第{i+1}个学生的年龄:"))
        db = Database.insert(db,name,age)
    return db

def query(db,id):
    """
    :param db: 数据库指针db
    :param id: 学生编号 id，(0代表所有学生)
    :return: 数据库指针db
    """
    results = Database.query(db,id)
    if not results:
        print(f"对不起，学生编号为【{id}】的学生不存在！")
        return db

    if not id:
        print("已查到所有学生信息，如下表：")
        print(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")

        for result in results:
            print(f"{result[0]:<6} {result[1]:<10} {result[2]:<4}")

    else:
        for result in results:
            print(" ".join(map(str,result)))

    return db
def show_menu():
    # 打印菜单栏
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

def menu(db):
    while True:
        op = input("请输入您的操作:")
        if op == "quit" or op == "0":
            Database.close(db)
            break
        elif op in ["i", "insert", "1"]:
            db = insert(db)
        elif op in ["q", "qa", "4", "5"]:
            if op in ["q", "4"]:
                id = int(input("请输入您要查询的学生编号(0代表所有学生)："))
                db = query(db, id)
            else:
                db = query(db, 0)
        elif op in ["d", "da", "2", "6"]:
            if op in ["d", "2"]:
                info = input("请输入您要删除的学生编号(0代表所有学生) 或 学生姓名：")
                db = Database.delete(db, info)
            else:
                db = Database.delete(db, "0")
        elif op in ["u", "3"]:
            id = int(input("请输入您要修改的学生编号："))
            modify_info = input("请输入新的数据(格式: 姓名 年龄)，若没有则输入:").split()
            db = Database.update(db, id, modify_info)


        elif op in ["c", " 7"]:
            print(f"学生总数: {Database.count(db)[0]}")

        elif op in ["p", "8"]:
            show_menu()
        else:
            continue


if __name__ == "__main__":
    # 创建数据库连接
    host = "localhost"
    user = "root"
    password = "Pass1234#"
    database = "test"

    db = Database.connect(host, user, password, database)

    menu(db)








