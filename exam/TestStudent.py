import pytest
from Manage import Manage
from Student import Student
from Logger import setup_logging

logger = setup_logging()

class TestStudent:

    @pytest.mark.parametrize("student_id,name,scores,average_score,grade",Manage("data.json").students)
    def test_student_add_score(self,student_id,name,scores,average_score,grade):
        logger.info(f"开始测试student.add_score: {student_id},{name},{scores},{average_score},{grade}")
        student = Student(student_id,name,scores)
        new = 85
        student.add_score(new)
        logger.info(f"添加新分数:{new}")
        scores.append(new)
        assert student.scores == scores

        logger.info(f"测试通过，预期结果：{student.scores}, 实际结果: {scores}")

    @pytest.mark.parametrize("student_id,name,scores,average_score,grade", Manage("data.json").students)
    def test_student_get_average(self,student_id,name,scores,average_score,grade):
        logger.info(f"开始测试student.add_score: {student_id},{name},{scores},{average_score},{grade}")
        student = Student(student_id, name, scores)

        assert student.get_average() == average_score

        logger.info(f"测试通过，预期结果：{student.get_average()}, 实际结果: {average_score}")

    @pytest.mark.parametrize("student_id,name,scores,average_score,grade", Manage("data.json").students)
    def test_student_get_grade(self,student_id,name,scores,average_score,grade):
        logger.info(f"开始测试student.add_score: {student_id},{name},{scores},{average_score},{grade}")
        student = Student(student_id, name, scores)

        assert student.get_grade() == grade

        logger.info(f"测试通过，预期结果：{student.get_grade()}, 实际结果: {grade}")
