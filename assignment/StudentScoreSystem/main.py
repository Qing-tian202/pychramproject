from System import System
from Logger import setup_logging

if __name__ == '__main__':
    logger = setup_logging()

    system = System(logger)
    system.start()

