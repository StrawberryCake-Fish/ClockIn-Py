import src
from typing import Optional
from loguru import logger


class CustomLogging:
    def __init__(self, log_path: Optional[str] = src.LOG_PATH):
        self.logger = logger
        self.logger.remove()
        self.logger.add(
            log_path, rotation='100 MB', encoding='utf-8',
            format='[{level}]-[{time:YYYY-MM-DD HH:mm:ss}]-[{thread.name}:{thread.id}]-[{file}:{line}] - {message}'
        )
        self.logger.add(
            lambda msg: print(msg, end=''), colorize=True,
            format='<green><level>[{level}]</level>-[{time:YYYY-MM-DD HH:mm:ss}]-'
                   '[{thread.name}:{thread.id}]-[{file}:{line}]</green> - <cyan>{message}</cyan>'
        )
