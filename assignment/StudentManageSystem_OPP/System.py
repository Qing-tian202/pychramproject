from Manager import Manager
from typing import Optional

class System:
    def __init__(self,logger, file_name: Optional[str] = 'add.json'):
        """
        实例化对象
        :param logger: 日志记录器
        :param file_name: 数据存放文件名
        """
        self.logger = logger
        self.file_name = file_name
        self.manager = Manager(logger, file_name)

    def start(self):
        """启动系统"""
        try:
            self.logger.info(f"开始运行系统")
            self.manager.run()
            self.logger.info(f"系统运行结束")
        except Exception as e:
            self.logger.error(f"系统运行过程出错：{e}")