from typing import NoReturn

from src.common import SingletonMeta
from src.event.event import ClockEvents
from src.handle.handle import StartHandler, CheckHandler, ClockHandler, RestartHandler, DoneHandler


class StartEvent(metaclass=SingletonMeta):
    _link = StartHandler()
    _link.set_next(CheckHandler()).set_next(ClockHandler()).set_next(RestartHandler()).set_next(
        DoneHandler())

    def _action(self, event: ClockEvents) -> NoReturn:
        result = self._link.handle(event)
        if isinstance(result, ClockEvents):
            self.link(result)

    def link(self, event: ClockEvents) -> NoReturn:
        self._action(event)
