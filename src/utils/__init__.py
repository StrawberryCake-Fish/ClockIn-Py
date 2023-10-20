import loguru
import src
from src.utils.log import CustomLogging
from src.utils.pool import ThreadPool

Logger: loguru = CustomLogging(src.LOG_PATH).logger
Task: ThreadPool = ThreadPool(5)
