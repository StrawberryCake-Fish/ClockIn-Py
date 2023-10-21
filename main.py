import time

from src.common.appium import AppiumStart, AppiumDriver
from src.event.event import ClockEvents
from src.event.start import StartEvent
from src.utils import Task, Logger


class Main:
    link = StartEvent()

    @classmethod
    def run(cls):
        # cls.link.link(ClockEvents.START)
        time.sleep(10)

        appium = AppiumDriver()
        appium.driver()
        Logger.info(appium.driver().current_activity)
        time.sleep(30)
        appium.quit()

        time.sleep(10)
        AppiumStart().kill()
        Task.wait_completion()


if __name__ == '__main__':
    Main.run()
