import argparse

import src
from src.utils.tools import Utils


class Env:
    src.CONF = Utils.load_json(src.CONFIG_PATH)

    def __getitem__(self, key):
        return self.__getattribute__(key)

    @staticmethod
    def argument():
        parser = argparse.ArgumentParser(
            prog='ClockIn',
            description='ClockIn Tools positional arguments',
            epilog='And What can I help U?'
        )
        parser.add_argument('--username', '-u', required=True, type=str, dest='username', help='Username.')
        parser.add_argument('--password', '-p', required=True, type=str, dest='password', help='Password.')
        args = parser.parse_args()
        src.USERNAME = args.username
        src.PASSWORD = args.password
