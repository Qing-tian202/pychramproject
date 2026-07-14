import DataBaseError

def insert(db,*args):
    """
    :param db: 数据库指针
    :param args: 姓名和年龄参数
    :return: 数据库指针db
    """
    while True:
        try:
            sql = f"insert into students (name, age) values (%s, %s)"
            cursor = db.cursor()

            cursor.execute(sql, args)

            if cursor.rowcount == 0:  # 更新的数据库条数为 0
                db.rollback()
                raise DataBaseError("数据库更新失败！")

            db.commit()
            cursor.close()
            #print("插入数据成功")
            return db
        except:
            raise
