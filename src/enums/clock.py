from enum import unique, Enum
from typing import NoReturn, Callable


class ClockAction:

    def login(self):
        pass


@unique
class ClockEnums(Enum):
    LOGIN = (ClockAction().login,)
    CHECK = (ClockAction().login,)
    CLOCK = (ClockAction().login,)
    RESTART = (ClockAction().login,)
    DONE = (ClockAction().login,)

    def __init__(self, action: Callable) -> NoReturn:
        self.action = action

    def do_action(self) -> NoReturn:
        self.action(self.name)
