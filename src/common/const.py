from enum import unique, Enum

from selenium.webdriver.common.by import By


@unique
class ConfigEnums(Enum):
    APPIUM_PORT = '4723'
    APPIUM_SECTION = 'appium'
    APPIUM_CONFIG = 'config'

    SIGN_PAGE = 'com.alibaba.android.user.login.SignUpWithPwdActivity'
    HOME_PAGE = '.biz.LaunchHomeActivity'
    CLOCK_PAGE = 'com.alibaba.lightapp.runtime.ariver.TheOneActivityMainTaskSwipe'


@unique
class ElementEnums(Enum):
    Via = (By.XPATH, '//*[@resource-id="com.alibaba.android.rimet:id/my_avatar"]')
    Username = (By.ID, 'com.alibaba.android.rimet:id/et_phone_input')
    Password = (By.ID, 'com.alibaba.android.rimet:id/et_password')
    Privacy = (By.ID, 'com.alibaba.android.rimet:id/cb_privacy')
    Login = (By.ID, 'com.alibaba.android.rimet:id/btn_next')

    Work = (By.XPATH, '//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]'
                      '/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    Clock = (By.XPATH, '//*[@text="\u8003\u52e4\u6253\u5361"]')
    State = (By.XPATH, '//*[contains(@text, "\u5df2\u6253\u5361")]')
    Close = (By.ID, 'com.alibaba.android.rimet:id/close_text')
