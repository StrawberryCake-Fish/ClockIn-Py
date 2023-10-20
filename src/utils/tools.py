import configparser
from typing import Any


class ParserToDict(configparser.ConfigParser):
    def dict(self):
        conf = dict(self._sections)
        for k in conf:
            conf[k] = dict(conf[k])
        return conf


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


class Utils:

    @staticmethod
    def dict_to_object(source: dict) -> dict | Dict[Any, Dict]:
        if not isinstance(source, dict):
            return source
        data = Dict()
        for k, v in source.items():
            data[k] = Utils.dict_to_object(v)
        return data
