import mysql.connector

def connect(hostname,user,passwd,database):
    """
    :param hostname: 主机名
    :param user: 用户名
    :param passwd: 密码
    :param database: 数据库
    :return: 数据库指针db
    """
    while True:
        try:
            # 创建数据库连接
            db = mysql.connector.connect(
                host=hostname,
                user=user,
                password=passwd,
                database=database
            )

            #print("数据库连接成功!")

            return db
        except mysql.connector.Error as e:
            #print(f"数据库连接失败:{e}")
            raise