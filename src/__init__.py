import datetime
import os

PROJECT = 'ClockIn-Py'

current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H')

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), PROJECT)
LOG_PATH = os.path.join(ROOT_PATH, 'logs', f'{current_date}.log')
CONFIG_PATH = os.path.join(ROOT_PATH, 'resources', 'config.ini')

CONF = None

USERNAME: str
PASSWORD: str
