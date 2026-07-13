
def delete(db, info):
    """
    :param db: 数据库指针db
    :param info: 学生编号(0代表所有学生) 或者 学生姓名
    :return: 数据库指针db
    """
    cursor = db.cursor()
    if info.isdigit():
        if int(info) == 0:
            cursor.execute("DELETE FROM students") # 删除所有数据
            cursor.execute("ALTER TABLE students AUTO_INCREMENT = 1") # 重置自增计数器
        else:
            sql = f"delete from students where id = %s"  #根据id删除指定数据
            cursor.execute(sql, [int(info)])
    else:
        sql = f"delete from students where name = %s" #根据名字删除
        cursor.execute(sql,[info])

    db.commit() #提交事务
    cursor.close()

    return db