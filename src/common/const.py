from enum import unique, Enum

from selenium.webdriver.common.by import By


class ConfigConst:
    APPIUM_SECTION = 'appium'
    APPIUM_CONFIG = 'config'

    SIGN_PAGE = 'com.alibaba.android.user.login.SignUpWithPwdActivity'
    HOME_PAGE = '.biz.LaunchHomeActivity'
    LOADING_PAGE = '.unihome.UniHomeLauncher'
    LAUNCHER_PAGE = '.launcher.Launcher'
    CLOCK_PAGE = 'com.alibaba.lightapp.runtime.ariver.TheOneActivityMainTaskSwipe'


@unique
class ElementEnums(Enum):
    Via = (By.XPATH, '//*[@resource-id="com.alibaba.android.rimet:id/my_avatar"]')
    Username = (By.ID, 'com.alibaba.android.rimet:id/et_phone_input')
    Password = (By.ID, 'com.alibaba.android.rimet:id/et_password')
    Privacy = (By.ID, 'com.alibaba.android.rimet:id/cb_privacy')
    Login = (By.ID, 'com.alibaba.android.rimet:id/btn_next')
    Clock = (By.XPATH, '//android.widget.LinearLayout['
                       '@resource-id="com.alibaba.android.rimet:id/tab_container"'
                       ']/android.widget.FrameLayout[4]')
    Close = (By.ID, 'com.alibaba.android.rimet:id/close_text')
