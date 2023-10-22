from src.event import Event
from src.utils import Task


class Main:
    def __init__(self):
        Event().argument()

    @staticmethod
    def run():
        Event().scheduler()
        Task.wait_completion()


if __name__ == '__main__':
    Main().run()
