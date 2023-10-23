import copy
import json
import os
import time
import src
from src.utils import Logger


class Utils:
    @staticmethod
    def banner():
        if os.path.exists(src.BANNER_PATH):
            for line in open(src.BANNER_PATH, 'r', encoding='utf-8'):
                Logger.info(line.replace('\n', ''))

    @staticmethod
    def load_json(file: str) -> dict:
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_start_time() -> tuple[str, list[str]]:
        ts = time.time()
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
        temp_ts = copy.deepcopy(ts) + 10
        temp_dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(temp_ts))
        return dt, temp_dt.split(' ')[1].split(':')
