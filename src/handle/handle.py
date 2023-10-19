from typing import NoReturn

from src.enums.clock import ClockEnums
from src.handle import AbstractHandler, Handler
from src.utils import Logger


class StartHandler(AbstractHandler):
    def handle(self, request: ClockEnums) -> Handler:
        if request == ClockEnums.LOGIN:
            Logger.info("Login...")
            super().handle(ClockEnums.CHECK)
        else:
            return super().handle(request)


class CheckHandler(AbstractHandler):
    def handle(self, request: ClockEnums) -> Handler:
        if request == ClockEnums.CHECK:
            Logger.info("Check...")
            super().handle(ClockEnums.RESTART)
        else:
            return super().handle(request)


class ClockHandler(AbstractHandler):
    def handle(self, request: ClockEnums) -> Handler:
        if request == ClockEnums.CLOCK:
            Logger.info("Clock...")
            super().handle(ClockEnums.DONE)
        else:
            return super().handle(request)


class RestartHandler(AbstractHandler):
    def handle(self, request: ClockEnums) -> Handler:
        if request == ClockEnums.RESTART:
            Logger.info("Restart...")
            super().handle(ClockEnums.CHECK)
        else:
            return super().handle(request)


class DoneHandler(AbstractHandler):
    def handle(self, request: ClockEnums) -> Handler:
        if request == ClockEnums.DONE:
            Logger.info("Done...")
        else:
            return super().handle(request)
