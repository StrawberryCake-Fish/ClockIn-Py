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
    APPIUM_PORT = '4723'
    APPIUM_SECTION = 'appium'
    APPIUM_CONFIG = 'config'
