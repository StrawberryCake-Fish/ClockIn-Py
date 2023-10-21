from src.event import Event
from src.strategy.action import StrategyEnums
from src.utils import Task


class Main:
    def __init__(self):
        Event().argument()

    @staticmethod
    def run():
        Event().link(StrategyEnums.START)
        Task.wait_completion()


if __name__ == '__main__':
    Main().run()
