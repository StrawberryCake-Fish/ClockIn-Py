from enum import unique, Enum


@unique
class ClockEnums(Enum):
    START = "START"
    CHECK = "CHECK"
    CLOCK = "CLOCK"
    RESTART = "RESTART"
    DONE = "DONE"
    EXIT = "EXIT"
