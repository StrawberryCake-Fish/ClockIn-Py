from src.enums.clock import ClockEnums
from src.handle import Handler
from src.handle.handle import CheckHandler, ClockHandler, RestartHandler, DoneHandler, StartHandler


class Main:

    @classmethod
    def run(cls):
        start: Handler = StartHandler()
        start.set_next(CheckHandler()).set_next(ClockHandler()).set_next(RestartHandler()).set_next(DoneHandler())
        start.handle(ClockEnums.LOGIN)
        # start.handle(ClockEnums.CHECK)


if __name__ == '__main__':
    Main.run()
