import mysql.connector
import random

class InsufficientFundsError(Exception):  #自定义异常
    pass

class DatabaseError(Exception):  #自定义异常
    pass

def valied_account(userid):
    """
    第一阶段：账户验证
    :param userid: 账户ID
    :return: 验证通过返回True，否则抛出ValueError
    """
    if not userid:
        raise ValueError("账户ID为空！")

    if not userid.isdigit():
        raise ValueError("账户ID必须为数字！")

    return True

def check_balance(db, userid, password, withdraw_money):
    """
    第二阶段：余额检查
    :param db: 数据库连接
    :param userid: 账户ID
    :param password: 密码
    :param withdraw_money: 取款金额
    :return: 当前余额
        """
    cursor = db.cursor()
    # 假设有一张表 users 存放账户信息，有 userid(账号), password(密码), balance(余额)
    cursor.execute("select balance from users where userid = %s and password = %s", (userid, password))
    result = cursor.fetchall()

    if not result:
        raise ValueError("账户不存在或密码错误")

    balance = result[0][0]

    if withdraw_money > balance:
        raise InsufficientFundsError(f"账户余额不足！ 当前账户余额 {balance}, 取款金额 {withdraw_money}")


    db.commit()
    cursor.close()

    return balance

def execute_transaction(db, username, password, withdraw_money, balance):
    """
    第三阶段：交易执行
    :param db: 数据库连接
    :param username: 账户ID
    :param password: 密码
    :param withdraw_money: 取款金额
    :param balance: 当前余额
    """
    try:
        cursor = db.cursor()

        new_balance = balance - withdraw_money

        cursor.execute("update users set balance = %s where userid = %s and password = %s", (new_balance,username,password))

        # 检查更新是否成功
        if cursor.rowcount == 0:
            raise DatabaseError("数据库更新失败！")

        #测试抛出数据库异常
        if random.randint(0,10) < 3:
            raise DatabaseError("数据库更新失败！")

        db.commit()
        cursor.close()

        print(f"交易成功！ 取款金额{withdraw_money}, 账户余额{new_balance}")

        return db

    except mysql.connector.Error as e:
        db.rollback() # 事务回滚
        print(f"数据库异常：{e}")

def function(db):
    """
    银行取款交易主函数
    :param db: 数据库连接
    :return: 数据库连接
    """
    try:
        cursor = db.cursor()

        # 输入账户信息
        userid = input("请输入账号：")
        password = input("请输入密码注意遮挡: ")

        # 第一阶段：账户验证
        if valied_account(userid):
            withdraw_money = int(input("请输入取款金额: "))  # 取款金额
            try:
                if withdraw_money <= 0:
                    raise ValueError("取款金额必须大于0！")

                if withdraw_money % 100 != 0:
                    raise ValueError("取款金额必须为100的整数倍！")
            except ValueError:
                print("请输入正确的取款金额！")

            #第二阶段：账户余额检查
            balance = check_balance(db, userid, password, withdraw_money)

            #第三阶段：交易执行
            db = execute_transaction(db, userid, password, withdraw_money, balance)

            db.commit()
            cursor.close()

    except ValueError as e:
        print(f"验证失败：{e}")
    except InsufficientFundsError as e:
        print(f"交易失败：{e}")
    except DatabaseError as e:
        print(f"系统错误：{e}")
    finally:
        return db




if __name__ == '__main__':
    try:
        host = "localhost"
        port = 3306
        user = "root"
        password = "Pass1234#"
        database = "test"

        db = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)

        db = function(db)

    except mysql.connector.Error as err:
        print(f"数据库连接错误: {err}")

    except Exception as e:
        print(f"系统异常：{e}")
    finally:
        if db and db.is_connected():
            db.close() #关闭数据库







