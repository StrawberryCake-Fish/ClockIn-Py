from __future__ import annotations
import argparse
import atexit
import src
from apscheduler.schedulers.background import BackgroundScheduler
from typing import NoReturn, Any
from src.common import SingletonMeta
from src.common.appium import AppiumStart
from src.strategy.action import StrategyEnums
from src.strategy.handle import StartHandler, ClockHandler, RestartHandler, DoneHandler
from src.utils import Logger


class Event(metaclass=SingletonMeta):
    def __init__(self):
        self._link = StartHandler()
        self._link.set_next(ClockHandler()).set_next(RestartHandler()).set_next(DoneHandler())

    def _action(self, event: StrategyEnums) -> NoReturn:
        result = self._link.handle(event)
        if isinstance(result, StrategyEnums):
            self.link(result)

    def link(self, event: StrategyEnums) -> NoReturn:
        self._action(event)

    def scheduler(self):
        Logger.info('Job start.')
        # src.Scheduler.add_job(self.link, trigger='cron', day_of_week='mon-fri', hour=9, minute=30,
        #                       args=[StrategyEnums.START])
        src.Scheduler.add_job(self.link, trigger='cron', second=0, minute=52, hour=18, args=[StrategyEnums.START])

    def __getitem__(self, key) -> Any:
        return self.__getattribute__(key)

    def argument(self) -> Event:
        parser = argparse.ArgumentParser(
            prog='ClockIn',
            description='ClockIn Tools positional arguments',
            epilog='And What can I help U?'
        )
        parser.add_argument('--username', '-u', required=True, type=str, dest='username', help='Username.')
        parser.add_argument('--password', '-p', required=True, type=str, dest='password', help='Password.')
        args = parser.parse_args()
        src.USERNAME = args.username
        src.PASSWORD = args.password
        return self

    @staticmethod
    @atexit.register
    def kill_appium():
        AppiumStart().kill()
