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


if __name__ == "__main__":
    question1()
    question2()