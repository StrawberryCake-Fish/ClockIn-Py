from __future__ import annotations
from enum import unique, Enum
from typing import NoReturn
from src.strategy import CommonContext
from src.strategy.action import Strategy, StartStrategy, CheckStrategy, ClockStrategy, RestartStrategy, DoneStrategy
from src.common.enums import ClockEnums


@unique
class ClockEvents(Enum):
    START = (StartStrategy(),)
    CHECK = (CheckStrategy(),)
    CLOCK = (ClockStrategy(),)
    RESTART = (RestartStrategy(),)
    DONE = (DoneStrategy(),)

    def __init__(self, event: Strategy) -> NoReturn:
        self.event = event

    def do_action(self) -> ClockEnums:
        CommonContext.strategy = self.event
        return CommonContext.do_business_logic()

    @staticmethod
    def get_event(enum: ClockEnums) -> ClockEvents | None:
        for i in ClockEvents:
            if i.name == enum.name:
                return i
        return None
