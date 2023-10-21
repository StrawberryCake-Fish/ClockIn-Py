from enum import unique, Enum


@unique
class ConfigEnums(Enum):
    APPIUM_PORT = '4723'
    APPIUM_SECTION = 'appium'
    APPIUM_CONFIG = 'config'

    LOGIN_PAGE = ''
    HOME_PAGE = '.biz.LaunchHomeActivity'
    CLOCK_PAGE = 'com.alibaba.lightapp.runtime.ariver.TheOneActivityMainTaskSwipe'


@unique
class ElementEnums(Enum):
    Via = '//*[@resource-id="com.alibaba.android.rimet:id/my_avatar"]'

    Work = ('//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]'
            '/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    Clock = '//*[@text="\u8003\u52e4\u6253\u5361"]'
    Close = '//*[@resource-id="com.alibaba.android.rimet:id/close_layout"]'
