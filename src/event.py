from __future__ import annotations
import argparse
import atexit
import src
from typing import NoReturn, Any
from src.common import SingletonMeta
from src.common.appium import AppiumStart
from src.strategy.action import StrategyEnums
from src.strategy.handle import StartHandler, ClockHandler, RestartHandler, DoneHandler
from src.utils import Logger
from src.utils.tools import Utils


class Event(metaclass=SingletonMeta):
    Utils.banner()

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
        if src.DBUG:
            temp = Utils.get_start_time()
            src.Scheduler.add_job(self.link, trigger='cron', second=int(temp[1][2]), minute=int(temp[1][1]),
                                  hour=int(temp[1][0]), args=[StrategyEnums.START])
            Logger.info(f'Starting time {temp[0]} delay to {temp[1][0]}:{temp[1][1]}:{temp[1][2]}.')
        else:
            src.Scheduler.add_job(self.link, trigger='cron', day_of_week='mon-fri', hour=9, minute=30,
                                  args=[StrategyEnums.START])

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
        parser.add_argument('--debug', '-d', required=False, action='store_true', dest='debug', help='Debug.')
        args = parser.parse_args()
        src.USERNAME = args.username
        src.PASSWORD = args.password
        src.DBUG = args.debug
        return self

    @staticmethod
    @atexit.register
    def kill_appium():
        AppiumStart().kill()
