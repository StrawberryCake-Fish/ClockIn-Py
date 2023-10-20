import time

from src.common.appium import AppiumStart
from src.event.event import ClockEvents
from src.event.start import StartEvent
from src.utils import Task


class Main:
    appium_event = AppiumStart()
    link = StartEvent()

    @classmethod
    def run(cls):
        cls.appium_event.start()
        cls.link.link(ClockEvents.START)
        time.sleep(10)
        cls.appium_event.kill()
        Task.wait_completion()


if __name__ == '__main__':
    Main.run()
