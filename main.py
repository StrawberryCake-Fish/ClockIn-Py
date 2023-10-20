from src.event.event import ClockEvents
from src.event.start import StartEvent
from src.utils import Logger


class Main:

    @classmethod
    def run(cls):
        Logger.info("Main.run!")
        StartEvent.link(ClockEvents.START)


if __name__ == '__main__':
    Main.run()
