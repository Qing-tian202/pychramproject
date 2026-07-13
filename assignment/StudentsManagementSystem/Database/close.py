import mysql.connector

def close(db):
    """
    :param db: 数据库指针
    :return: 数据库指针db
    """
    while True:
        try:
            if db is None:
                #print("警告: 数据库连接对象为 None，无需关闭")
                return True

            # 检查连接是否仍然活跃
            if hasattr(db, 'is_connected') and db.is_connected():
                db.close()
                #print(" 数据库连接已成功关闭")
                return True
            else:
                #print(" 数据库连接已经关闭或无效")
                return True

        except mysql.connector.Error as e:
            #print(f" 数据库关闭错误 (MySQL错误): {e}")
            #print(f"   错误代码: {e.errno}")
            #print(f"   SQL状态: {e.sqlstate}")
            return False

        except AttributeError as e:
            #print(f" 数据库对象无效: {e}")
            #print("   请确保传入的是有效的数据库连接对象")
            return False

        except Exception as e:
            #print(f" 关闭数据库时发生未知错误: {type(e).__name__}")
            #print(f"   错误信息: {e}")
            import traceback
            #print("   详细堆栈:")
            traceback.print_exc()
            return False