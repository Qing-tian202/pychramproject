"""
你有一个包含学生成绩的字符串列表，每个学生的成绩格式如下：
"姓名 成绩"
例如：
students_scores = [  
    "Alice 85",  
    "Bob 92",  
    "Charlie 78",  
    "David 90",  
    "Eva 88"  
]
请完成以下任务：
1. 提取姓名和成绩：
  ○ 创建一个新的列表，其中包含学生的姓名和对应的成绩，但这次我们使用两个独立的列表来存储姓名和成绩。
2. 计算平均成绩：
  ○ 计算所有学生的平均成绩（保留两位小数）。
3. 找出最高分和最低分：
  ○ 找出最高分和最低分，并打印出对应的分数（并打印学生姓名）。
4. 按成绩排序：
  ○ 将学生按成绩从高到低排序，并打印排序后的成绩列表。为了匹配排序后的成绩，你也可以打印出排序后的姓名列表。
5. 过滤成绩：
  ○ 过滤出成绩在80分及以上的学生姓名，并返回这些姓名列表。

"""
def print_score():
    students_scores = ["Alice 85","Bob 92","Charlie 78","David 90","Eva 88"]
    students_scores = [x.split( ) for x in students_scores]
    students_scores.sort(key = lambda x:-int(x[1]))
    
    names = []
    scores = []
    count = 0
    for name,score in students_scores:
        names.append(name)
        scores.append(int(score))
        if int(score) >= 80:
            count += 1

    print(f"成绩列表{scores}")
    print(f"分数大于80分的学生姓名：{names[:count]}")
    print(f"平均成绩{float(sum(scores)/len(scores))}")
    print(f"最高分是 {students_scores[0][0]},{students_scores[0][1]}, 最低分是 {students_scores[-1][0]},{students_scores[-1][1]}")
    print(f"成绩列表{scores}")
    print(f"分数大于80分的学生姓名：{names[:count]}")


if __name__ == "__main__":
    print_score()