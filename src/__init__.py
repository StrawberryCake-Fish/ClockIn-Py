import datetime
import os

PROJECT: str = 'ClockIn-Py'

current_date: str = datetime.datetime.now().strftime('%Y-%m-%d')

ROOT_PATH: str = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), PROJECT)
LOG_PATH: str = os.path.join(ROOT_PATH, 'logs', f'{current_date}.log')
CONFIG_PATH: str = os.path.join(ROOT_PATH, 'resources', 'config.json')

CONF: dict
USERNAME: str
PASSWORD: str
