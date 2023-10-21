from enum import unique, Enum


@unique
class ConfigEnums(Enum):
    APPIUM_PORT = '4723'
    APPIUM_SECTION = 'appium'
    APPIUM_CONFIG = 'config'

    LOGIN_PAGE = ''
    HOME_PAGE = '.biz.LaunchHomeActivity'
    CLOCK_PAGE = 'com.alibaba.lightapp.runtime.ariver.TheOneActivityMainTaskSwipe'
