from typing import NoReturn
from src.event.event import ClockEvents
from src.handle.handle import StartHandler, CheckHandler, ClockHandler, RestartHandler, DoneHandler


class StartEvent:
    _link = StartHandler()
    _link.set_next(CheckHandler()).set_next(ClockHandler()).set_next(RestartHandler()).set_next(
        DoneHandler())

    @classmethod
    def _action(cls, event: ClockEvents) -> NoReturn:
        result = cls._link.handle(event)
        if isinstance(result, ClockEvents):
            cls.link(result)

    @classmethod
    def link(cls, event: ClockEvents) -> NoReturn:
        cls._action(event)
