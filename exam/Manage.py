from Logger import setup_logging
import json
import traceback
import os

logger = setup_logging()

class Manage:
    def __init__(self, file_name):
        self.file_name = file_name
        self.students = []
        self.load_data()

    def load_data(self):
        """载入数据"""
        try:
            logger.info(f"开始载入数据")
            if not os.path.exists(self.file_name):
                raise FileNotFoundError(f"文件不存在：{self.file_name}")

            with open(self.file_name, "r", encoding='utf-8') as f:
                data = json.load(f)

                for item in data:
                    student = [item.get("student_id"),
                               item.get("name"),
                               item.get("scores"),
                               item.get("average_score"),
                               item.get("grade")
                              ]
                    self.students.append(student)
            logger.info(f"载入数据成功：{self.students}")
        except FileNotFoundError as e:
            logger.error(f"载入数据失败：{e}")
        except json.JSONDecodeError:
            logger.error(f"载入数据失败, 文件 {self.file_name} 格式错误，将重新创建")
            self.save_data(False)
        except Exception as e:
            logger.error(f"载入数据发生错误：{e} \n {traceback.format_exc()}")


    def save_data(self, flage = True):
        """
                保存数据
                :param flage: 是否需要创建新文件，默认不需要
                :return:
                """
        if flage:
            try:
                logger.info(f"开始保存数据")
                if self.students:
                    with open(self.file_name, "w", encoding='utf-8') as f:
                        data = [student for student in self.students]
                        json.dump(data, f, ensure_ascii=False, indent=4)
                        logger.info(f"保存数据成功：{data}")

                else:
                    logger.warning(f"没有数据需要保存")
            except Exception as e:
                logger.error(f"保存数据发生错误：{e} \n {traceback.format_exc()}")

        else:
            try:
                logger.info(f"开始创建新文件")
                with open(self.file_name, "w", encoding='utf-8') as f:
                    json.dump([], f, ensure_ascii=False, indent=4)
                logger.info(f"创建文件成功")
            except Exception as e:
                logger.error(f"创建文件失败：{e} \n {traceback.format_exc()}")
