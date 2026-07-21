from Logger import setup_logging

logger = setup_logging()

def validate_score(func):
    def wrapper(*args, **kwargs):
        try:
            score = args[1]
            if score < 0 or score > 100:
                raise ValueError(f"无效分数：{score}")
            return func(*args, **kwargs)

        except ValueError as e:
            logger.error(f" 请输入正确的分数(0 - 100) : {e}")

    return wrapper




class Student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id
        self.name = name
        self.scores = [score for score in scores]

    @validate_score
    def add_score(self, score):
        logger.info(f"成功添加成绩：{score}")
        self.scores.append(score)

    def get_average(self):
        if not self.scores:
            logger.info(f"成绩列表为空，平均成绩为0")
            return 0
        avg_score = round(sum(self.scores)/len(self.scores), 2)
        logger.info(f"平均成绩：{avg_score}")
        return avg_score

    def get_grade(self):
        score = self.get_average()
        if score >= 90:
            logger.info(f"当前平均分：{score}, 等级 A")
            return "A"
        elif score >= 80:
            logger.info(f"当前平均分：{score},等级 B")
            return "B"
        elif score >= 70:
            logger.info(f"当前平均分：{score},等级 C")
            return "C"
        elif score >= 60:
            logger.info(f"当前平均分：{score},等级 D")
            return "D"
        else:
            logger.info(f"当前平均分：{score},等级 F")
            return "F"
