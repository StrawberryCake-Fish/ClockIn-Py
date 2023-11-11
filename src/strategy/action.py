from __future__ import annotations
import random
import time

from appium.webdriver import WebElement

import src
from enum import Enum, unique
from typing import NoReturn
from src.common.appium import AppiumDriver
from src.common.const import ElementEnums
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
        if src.DBUG is False:
            time.sleep(random.randint(2, 6) * 60)
        try:
            if driver.wait(ElementEnums.Via.value) is False:
                driver.wait(ElementEnums.Username.value).send_keys(src.USERNAME)
                driver.wait(ElementEnums.Password.value).send_keys(src.PASSWORD)
                driver.wait(ElementEnums.Privacy.value).click()
                driver.wait(ElementEnums.Login.value).click()
            return StrategyEnums.CLOCK
        except Exception as e:
            Logger.error(e)
            return StrategyEnums.RESTART


class ClockStrategy(Strategy):
    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Logger.info("ClockStrategy.do_action")
        try:
            clock_element = driver.wait(ElementEnums.Clock.value, 2)
            if isinstance(clock_element, WebElement):
                clock_element.click()
            else:
                return StrategyEnums.DONE

            close_element = driver.wait(ElementEnums.Close.value, 2)
            if isinstance(close_element, WebElement):
                close_element.click()
                return StrategyEnums.CLOCK
            return StrategyEnums.DONE
        except Exception as e:
            Logger.error(e)
            return StrategyEnums.RESTART


class RestartStrategy(Strategy):
    def action(self, driver: AppiumDriver) -> StrategyEnums:
        Logger.info("RestartStrategy.do_action")
        try:
            driver.restart()
        except Exception as e:
            Logger.error(e)
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
