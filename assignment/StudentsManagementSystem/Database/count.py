
def count(db):
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM students")

    result = cursor.fetchall()
    cursor.close()

    return result[0]