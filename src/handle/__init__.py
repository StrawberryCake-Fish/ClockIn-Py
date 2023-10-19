from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from src.enums.clock import ClockEnums
from src.utils import Logger


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: ClockEnums) -> Handler:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: ClockEnums) -> Handler:
        if self._next_handler:
            return self._next_handler.handle(request)
        Logger.info("End!")
