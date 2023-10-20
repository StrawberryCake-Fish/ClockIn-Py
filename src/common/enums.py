from enum import unique, Enum


@unique
class ClockEnums(Enum):
    START = 'START'
    CHECK = 'CHECK'
    CLOCK = 'CLOCK'
    RESTART = 'RESTART'
    DONE = 'DONE'
    EXIT = 'EXIT'


@unique
class ConfigEnums(Enum):
    APPIUM_SECTION = 'appium'
    ACCOUNT_SECTION = 'account'
