from __future__ import annotations

import random
import time
from abc import ABC, abstractmethod

import src
from src.common.appium import AppiumStart, AppiumDriver
from src.common.const import ConfigEnums
from src.strategy.action import StrategyEnums, StrategyAction
from src.utils import Logger


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: StrategyEnums) -> Handler:
        pass


class AbstractHandler(Handler):
    AppiumStart().start()
    appium = AppiumDriver()
    wait = True
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if self._next_handler:
            return self._next_handler.handle(request)
        Logger.info("Link exit!")
        return request


class StartHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.START:
            Logger.info(f'StartHandler {request.name}')
            try:
                if src.DBUG is False and self.wait:
                    time.sleep(random.randint(2, 6) * 60)
                    self.wait = False
                activity = self.appium.driver().current_activity
                Logger.info(f'Activity {activity}')
                match activity:
                    case ConfigEnums.SIGN_PAGE.value:
                        return super().handle(StrategyAction.find(request).action(self.appium))
                    case ConfigEnums.HOME_PAGE.value:
                        return super().handle(StrategyAction.find(request).action(self.appium))
                    case ConfigEnums.CLOCK_PAGE.value:
                        return super().handle(StrategyEnums.CLOCK)
                    case _:
                        return super().handle(StrategyEnums.DONE)
            except Exception as e:
                Logger.error(e)
                return StrategyEnums.RESTART
        else:
            return super().handle(request)


class ClockHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.CLOCK:
            Logger.info(f'ClockHandler {request.name}')
            return super().handle(StrategyAction.CLOCK.action(self.appium))
        else:
            return super().handle(request)


class RestartHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.RESTART:
            Logger.info(f'RestartHandler {request.name}')
            return super().handle(StrategyAction.RESTART.action(self.appium))
        else:
            return super().handle(request)


class DoneHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.DONE:
            Logger.info(f'DoneHandler {request.name}')
            self.appium.quit()
            self.wait = True
        else:
            return super().handle(request)
