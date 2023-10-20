from abc import ABC, abstractmethod
from typing import NoReturn

from src.common.enums import ClockEnums
from src.utils import Logger


class Strategy(ABC):

    @abstractmethod
    def do_action(self) -> NoReturn:
        Logger.info("Strategy.do_action!")


class StartStrategy(Strategy):
    def do_action(self) -> ClockEnums:
        Logger.info("StartStrategy.do_action!")
        return ClockEnums.CHECK


class CheckStrategy(Strategy):
    def do_action(self) -> ClockEnums:
        Logger.info("CheckStrategy.do_action!")
        return ClockEnums.DONE


class ClockStrategy(Strategy):
    def do_action(self) -> ClockEnums:
        Logger.info("ClockStrategy.do_action!")
        return ClockEnums.DONE


class RestartStrategy(Strategy):
    def do_action(self) -> ClockEnums:
        Logger.info("RestartStrategy.do_action!")
        return ClockEnums.DONE


class DoneStrategy(Strategy):
    def do_action(self) -> ClockEnums:
        Logger.info("DoneStrategy.do_action!")
        return ClockEnums.EXIT
