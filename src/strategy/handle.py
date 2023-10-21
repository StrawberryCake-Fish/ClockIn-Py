from __future__ import annotations
from abc import ABC, abstractmethod
from typing import NoReturn

from appium.webdriver.webdriver import WebDriver
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
    _appium = AppiumDriver()
    _next_handler: Handler = None

    def get_driver(self) -> WebDriver:
        return self._appium.driver()

    def done(self) -> NoReturn:
        self._appium.quit()

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
            activity = self.get_driver().current_activity
            match activity:
                case ConfigEnums.HOME_PAGE.value:
                    return super().handle(StrategyEnums.CLOCK)
                case ConfigEnums.CLOCK_PAGE.value:
                    return super().handle(StrategyEnums.CLOCK)
                case ConfigEnums.LOGIN_PAGE.value:
                    return super().handle(StrategyAction.find(request).action())
        else:
            return super().handle(request)


class ClockHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.CLOCK:
            Logger.info(f'ClockHandler {request.name}')
            return super().handle(StrategyAction.CLOCK.action())
        else:
            return super().handle(request)


class RestartHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.RESTART:
            Logger.info(f'RestartHandler {request.name}')
            return super().handle(StrategyAction.RESTART.action())
        else:
            return super().handle(request)


class DoneHandler(AbstractHandler):
    def handle(self, request: StrategyEnums) -> Handler | StrategyEnums:
        if request == StrategyEnums.DONE:
            Logger.info(f'DoneHandler {request.name}')
            self.done()
        else:
            return super().handle(request)
