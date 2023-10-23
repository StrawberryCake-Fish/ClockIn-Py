import datetime
import json
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import BaseScheduler

PROJECT: str = 'ClockIn-Py'

current_date: str = datetime.datetime.now().strftime('%Y-%m-%d')

ROOT_PATH: str = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), PROJECT)
LOG_PATH: str = os.path.join(ROOT_PATH, 'logs', f'{current_date}.log')
BANNER_PATH: str = os.path.join(ROOT_PATH, 'resources', 'banner.txt')
CONFIG_PATH: str = os.path.join(ROOT_PATH, 'resources', 'config.json')

CONF: dict
with open(CONFIG_PATH, encoding='utf-8') as f:
    CONF = json.load(f)

USERNAME: str
PASSWORD: str
DBUG: bool

Scheduler: BaseScheduler = BackgroundScheduler()
Scheduler.start()
