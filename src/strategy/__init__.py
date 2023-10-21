from __future__ import annotations
from abc import ABC, abstractmethod
from typing import NoReturn, Any
from src.common import SingletonMeta
from src.utils import Logger


class Strategy(ABC):

    @abstractmethod
    def action(self) -> NoReturn:
        Logger.info("Strategy.do_action!")


class Context(metaclass=SingletonMeta):
    def __init__(self) -> NoReturn:
        self._strategy = None

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, event: Strategy) -> NoReturn:
        self._strategy = event

    def do_business_logic(self) -> Any:
        return self._strategy.action()
