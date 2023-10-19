import loguru
import src
from src.utils.log import CustomLogging

Logger: loguru = CustomLogging(src.LOG_PATH).logger
