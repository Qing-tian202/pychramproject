from MGraph import MGraph
from linklist import linklist


"""
练习
1.提示用户输入两个数字
2.使用获取到的数据进行加法运算
3.在控制台输出计算结果，格式要求：xx + xx = xx
"""
def question1():
    x = int(input("please input a number: "))
    y = int(input("please input a number: "))
    print(f"{x} + {y} = {x+y}")
    return


"""
1. 提示用户输入用户姓名，并保存到变量中
2. 提示用户输入用户年龄，保存到变量中，并转换成整数
3. 提示用户输入用户身高，保存到变量中，并转换成浮点数
4. 在控制台输出用户姓名、年龄、身高对应变量的数据类型
5. 按照以下格式输出用户信息：“姓名:xxx 年龄:xxx 身高:xxx”
6. 在控制台输出该用户5年之后的年龄，格式：“张三 5 年之后的年龄是 25”
7. 在控制台输出该用户现在是否成年，格式：“张三是否成年：True”
"""

def question2():
    name = input("please input name :")
    age = int(input("please input age:"))
    height = float(input("please input height: "))

    print(f"姓名的数据类型:{type(name)} 年龄的数据类型:{type(age)} 身高的数据类型:{type(height)}")
    print(f"姓名:{name} 年龄:{age} 身高:{height}")
    print(f"{name} 5年之后的年龄是 {age + 5}")
    print(f"{name} 是否成年 {age >= 18}")


"""
1. 程序启动时显示欢迎信息："欢迎使用用户登录系统"
2. 提示用户输入用户名和密码
3. 验证用户名和密码是否正确（正确的用户名：admin，密码：123456）
4. 如果用户名和密码都正确：
  ○ 打印"登录成功！"
  ○ 结束程序
5. 如果用户名或密码错误：
  ○ 打印"用户名或密码错误！"
  ○ 提示用户继续输入用户名和密码
6. 特殊退出功能：
  ○ 如果用户输入的用户名为"exit"（不区分大小写）
  ○ 打印"程序已退出"
  ○ 结束程序
7. 增加尝试次数限制：
  ○ 用户最多有5次尝试机会
  ○ 每次尝试失败后显示剩余尝试次数
  ○ 当尝试次数用尽时，打印"尝试次数已达上限，系统已锁定！"并结束程序

"""


def login():
    time = 5
    while time > 0:
        usrname = input("请输入用户名：")
        passwd = input("请输入密码：")
        if usrname == 'exit' or usrname == 'EXIT':
            print("程序已退出")
            return
        elif usrname == "admin" and passwd == "123456":
            print("登录成功！")
            return
        else:
            time -= 1
            print(f"用户名或密码错误！剩余尝试次数{time}")

    print("尝试次数已达上限，系统已锁定")
    return

def question3():
    print("欢迎使用用户登录系统")
    login()


"""
你有一个包含学生成绩的字符串列表，每个学生的成绩格式如下：
"姓名 成绩"
例如：
students_scores = [  
    "Alice 85",  
    "Bob 92",  
    "Charlie 78",  
    "David 90",  
    "Eva 88"  
]
请完成以下任务：
1. 提取姓名和成绩：
  ○ 创建一个新的列表，其中包含学生的姓名和对应的成绩，但这次我们使用两个独立的列表来存储姓名和成绩。
2. 计算平均成绩：
  ○ 计算所有学生的平均成绩（保留两位小数）。
3. 找出最高分和最低分：
  ○ 找出最高分和最低分，并打印出对应的分数（并打印学生姓名）。
4. 按成绩排序：
  ○ 将学生按成绩从高到低排序，并打印排序后的成绩列表。为了匹配排序后的成绩，你也可以打印出排序后的姓名列表。
5. 过滤成绩：
  ○ 过滤出成绩在80分及以上的学生姓名，并返回这些姓名列表。

"""

def question4():
    students_scores = ["Alice 85", "Bob 92", "Charlie 78", "David 90", "Eva 88"]
    students_scores = [x.split() for x in students_scores]
    students_scores.sort(key=lambda x: -int(x[1]))

    names = []
    scores = []
    count = 0
    for name, score in students_scores:
        names.append(name)
        scores.append(int(score))
        if int(score) >= 80:
            count += 1

    print(f"学生姓名：{names}")
    print(f"成绩：{scores}")
    print(f"平均成绩{float(sum(scores) / len(scores)):.2f}")
    print(f"最高分是 {students_scores[0][0]},{students_scores[0][1]}, 最低分是 {students_scores[-1][0]},{students_scores[-1][1]}")
    print(f"成绩列表{scores}")
    print(f"分数大于80分的学生姓名：{names[:count]}")

def fibona(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibona(n-1) + fibona(n-2)

if __name__ == "__main__":
    a = [[1] * 3 for _ in range(3)]
    b = []
    c = []
    for i in range(3):
        b.append(a[i])
        c.extend(a[i])
    print(b)
    print(c)

    print(fibona(5)) #1, 1, 2, 3, 5, 8
    print("-------------------------")
    print(" 0:exit; \n 1:question1; \n 2:question2; \n 3:question3 \n ")
    print("-------------------------")
    n = int(input("please input nuber: "))
    if n==0:
        pass
    elif n ==1:
        question1()
    elif n == 2:
        question2()
    elif n == 3:
        question3()
    elif n == 4:
        question4()
    else:
        pass