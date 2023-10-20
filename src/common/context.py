from typing import NoReturn, Any
from src.common.strategy import Strategy
from src.event.enums import ClockEnums


class Context:
    def __init__(self, strategy: Strategy) -> NoReturn:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, event: Strategy) -> NoReturn:
        self._strategy = event

    def do_business_logic(self) -> ClockEnums:
        return self._strategy.do_action()
