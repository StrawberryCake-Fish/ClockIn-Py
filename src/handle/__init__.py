from __future__ import annotations
from abc import ABC, abstractmethod

from appium.webdriver.webdriver import WebDriver

from src.common.appium import AppiumDriver, AppiumStart
from src.event.event import ClockEvents
from src.utils import Logger


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: ClockEvents) -> Handler:
        pass


class AbstractHandler(Handler):
    AppiumStart().start()
    _appium = AppiumDriver()
    _next_handler: Handler = None

    def get_driver(self) -> WebDriver:
        return self._appium.driver()

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: ClockEvents) -> Handler | ClockEvents:
        if self._next_handler:
            return self._next_handler.handle(request)
        Logger.info("Link exit!")
        return request
