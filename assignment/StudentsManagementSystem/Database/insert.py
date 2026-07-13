

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
            db.commit()
            cursor.close()
            #print("插入数据成功")
            return db
        except:
            raise
