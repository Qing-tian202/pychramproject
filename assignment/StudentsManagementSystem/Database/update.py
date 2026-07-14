import DataBaseError


def update(db, *args):
    """
        :param db: 数据库指针
        :param args: 其余参数：id，name，age，op
        :return: 数据库指针db
        """
    cursor = db.cursor()
    id, other = args #分离参数

    if len(other) == 2: #要修改名字和年龄
        name, age = other
        sql = f"update students set name = %s, age = %s where id = %s"
        cursor.execute(sql, [name, int(age), id])
    else:
        if other[0].isalpha(): #只修改名字
            sql = f"update students set name = %s where id = %s"
            cursor.execute(sql, [other[0], id])
        else:  #只修改年龄
            sql = f"update students set age = %s where id = %s"
            cursor.execute(sql, [int(other[0]), id])

    if cursor.rowcount == 0: #更新的数据库条数为 0
        db.rollback()
        raise DataBaseError("数据库更新失败！")

    db.commit()
    cursor.close()
    #print("修改成功！")
    return db
