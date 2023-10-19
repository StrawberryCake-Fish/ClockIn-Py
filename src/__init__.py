import datetime
import os

PROJECT = 'ClockIn-Py'

current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H')
dir_name = current_date.split('_')[0]

ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), PROJECT)
LOG_PATH = os.path.join(ROOT_PATH, 'logs', dir_name, f'{current_date}.log')
