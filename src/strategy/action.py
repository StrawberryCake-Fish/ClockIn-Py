from __future__ import annotations
from enum import Enum, unique
from typing import NoReturn
from src.strategy import Strategy, Context
from src.utils import Logger


@unique
class StrategyEnums(Enum):
    START = 'START'
    CLOCK = 'CLOCK'
    RESTART = 'RESTART'
    DONE = 'DONE'


class StartStrategy(Strategy):
    def action(self) -> StrategyEnums:
        Logger.info("StartStrategy.do_action!")
        # TODO 执行登录操作，输入账号密码点击登录
        return StrategyEnums.CLOCK


class ClockStrategy(Strategy):
    def action(self) -> StrategyEnums:
        Logger.info("ClockStrategy.do_action!")
        return StrategyEnums.DONE


class RestartStrategy(Strategy):
    def action(self) -> StrategyEnums:
        Logger.info("RestartStrategy.do_action!")
        return StrategyEnums.DONE


class DoneStrategy(Strategy):
    def action(self) -> StrategyEnums:
        Logger.info("DoneStrategy.do_action!")
        return StrategyEnums.DONE


@unique
class StrategyAction(Enum):
    START = (StartStrategy(),)
    CLOCK = (ClockStrategy(),)
    RESTART = (RestartStrategy(),)
    DONE = (DoneStrategy(),)

    def __init__(self, event: Strategy) -> NoReturn:
        self.event = event

    @staticmethod
    def find(source: StrategyEnums) -> StrategyAction:
        for i in StrategyAction:
            if i.name == source.name:
                return i
            else:
                raise TimeoutError('StrategyAction find not found!')

    def action(self) -> StrategyEnums:
        Context().strategy = self.event
        return Context().do_business_logic()
