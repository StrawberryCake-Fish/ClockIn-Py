from __future__ import annotations
from enum import Enum, unique
from typing import NoReturn

from selenium.webdriver.common.by import By

import src
from src.common.appium import AppiumDriver
from src.common.const import ElementEnums, ConfigEnums
from src.strategy import Strategy, Context
from src.utils import Logger


@unique
class StrategyEnums(Enum):
    START = 'START'
    CLOCK = 'CLOCK'
    RESTART = 'RESTART'
    DONE = 'DONE'


class StartStrategy(Strategy):
    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Logger.info("StartStrategy.do_action")
        # TODO 执行登录操作，输入账号密码点击登录
        return StrategyEnums.CLOCK


class ClockStrategy(Strategy):
    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Logger.info("ClockStrategy.do_action")
        try:
            driver.wait((By.XPATH, ElementEnums.Work.value)).click()
            driver.wait((By.XPATH, ElementEnums.Clock.value)).click()
        except Exception as e:
            Logger.error(e)
            return StrategyEnums.RESTART
        return StrategyEnums.DONE


class RestartStrategy(Strategy):
    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Logger.info("RestartStrategy.do_action")
        try:
            driver.restart()
        except Exception as e:
            Logger.error(e)
            driver.driver()
        return StrategyEnums.START


@unique
class StrategyAction(Enum):
    START = (StartStrategy(),)
    CLOCK = (ClockStrategy(),)
    RESTART = (RestartStrategy(),)

    def __init__(self, event: Strategy) -> NoReturn:
        self.event = event

    @staticmethod
    def find(source: StrategyEnums) -> StrategyAction:
        for i in StrategyAction:
            if i.name == source.name:
                return i
            else:
                raise TimeoutError('StrategyAction find not found!')

    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Context().strategy = self.event
        return Context().do_business_logic(driver)
