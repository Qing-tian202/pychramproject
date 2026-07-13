"""
石头剪刀布 0,1,2  Rock-paper-scissors

系统接收人输入，系统随机数字，判断谁胜谁负
"""
import random

def fun():
    x = random.randint(0, 2)
    y = int(input("请输入（0:石头，1:剪刀，2:布）："))
    result = (x , y)
    #print(result)
    if result == (0,2) or result == (1 , 0) or result == (2 , 1):
        print("你赢了！")
    elif result==(0, 0) or result == (1 , 1) or result == ( 2, 2):
        print("平局！")
    else:
        print("你输了！")

if __name__ == "__main__":
    fun()