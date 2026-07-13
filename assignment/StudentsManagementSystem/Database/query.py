
def query(db,id):
    """
    :param db: 数据库指针
    :param id: 学生编号 id，(0代表所有学生)
    :return: 查询结果[列表]
    """
    cursor = db.cursor()

    if id: #指定编号
        sql = f"select * from students where id = %s"
        cursor.execute(sql, [id])
    else:
        sql = f"select * from students"
        cursor.execute(sql,[])

    # 获取查询结果
    results = cursor.fetchall()
    cursor.close()

    return results