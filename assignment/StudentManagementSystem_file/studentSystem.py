import os

def insert(dataframe):
    n = int(input("您要新增几条数据，请输入:"))
    if not dataframe:
        for i in range(n):
            name = input(f"请输入第{i + 1}个学生的名字:")
            age = input(f"请输入第{i + 1}个学生的年龄:")
            dataframe.append([i+1, name, age])
    else:
        id, _, _ = dataframe[-1]
        for i in range(n):
            name = input(f"请输入第{i + 1}个学生的名字:")
            age = input(f"请输入第{i + 1}个学生的年龄:")
            dataframe.append([i+1+id, name, age])

    return dataframe


def query(dataframe,id):
    if not id:
        print("已查到所有学生信息，如下表：")
        print(f"{'编号':<6} {'姓名':<10} {'年龄':<4}")

        for result in dataframe:
            # result = result.split(",")
            print(f"{result[0]:<6} {result[1]:<10} {result[2]:<4}")


    else:
        flag = 0
        for result in dataframe:
            if result[0] == id:
                print(" ".join(map(str,result)))
                flag = 1
        if not flag:
            print(f"对不起，学生编号为【{id}】的学生不存在！")

    return dataframe


def delete(dataframe,info):
    if info.isdigit():
        if info == "0":
            return []
        else:
            for i in range(len(dataframe)):
                if int(info) == dataframe[i][0]:
                    dataframe.pop(i)

    else:
        for i in range(len(dataframe)):
            if int(info) == dataframe[i][1]:
                dataframe.pop(i)

    return dataframe




def update(dataframe,id,modify_info):
    if len(modify_info) == 2:
        for i in range(len(dataframe)):
            if id == dataframe[i][0]:
                dataframe[i][1], dataframe[i][2] = modify_info[0], modify_info[1]

    else:
        if modify_info[0].isalpha():
            for i in range(len(dataframe)):
                if id == dataframe[i][0]:
                    dataframe[i][1] =  modify_info[0]
        else:
            for i in range(len(dataframe)):
                if id == dataframe[i][0]:
                    dataframe[i][2] =  modify_info[1]

    return dataframe


def count(dataframe):
    print(f"学生总数: {len(dataframe)}")
    return dataframe


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

def menu(dataframe):
    while True:
        op = input("请输入您的操作:")
        if op in ["quit", "0"]:
            return dataframe
        elif op in ["i", "insert", "1"]:
            dataframe = insert(dataframe)
        elif op in ["q", "qa", "4", "5"]:
            if op in ["q", "4"]:
                id = int(input("请输入您要查询的学生编号(0代表所有学生)："))
                dataframe = query(dataframe,id)
            else:
                dataframe = query(dataframe,0)
        elif op in ["d", "da", "2", "6"]:
            if op in ["d", "2"]:
                info = input("请输入您要删除的学生编号(0代表所有学生) 或 学生姓名：")
                dataframe = delete(dataframe,info)
            else:
                dataframe = delete(dataframe,"0")
        elif op in ["u", "3"]:
            id = int(input("请输入您要修改的学生编号："))
            modify_info = input("请输入新的数据(格式: 姓名 年龄)，若没有则输入:").split( )
            dataframe = update(dataframe,id,modify_info)

        elif op in ["c", " 7"]:
            dataframe = count(dataframe)

        elif op in ["p", "8"]:
            show_menu()

        else:
            continue




if __name__ == "__main__":
    file_name = r'data.txt'
    df = []

    if not os.path.exists(file_name):
        with open(file_name, 'a', encoding= 'utf-8') as f:
            pass
    else:
        with open(file_name, 'r', encoding='utf-8') as f:
            df = f.readlines()

    show_menu()
    df = menu(df)
    # print(df)

    if df:
        with open(file_name, 'w', encoding='utf-8') as f:
            for data in df:
                f.write(",".join(map(str,data)))

    #print("operation over!")