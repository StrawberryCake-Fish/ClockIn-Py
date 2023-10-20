import argparse

import src
from src.utils.tools import ParserToDict


class Env:
    src.CONF = ParserToDict()
    src.CONF.read(src.CONFIG_PATH, 'utf-8')

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
