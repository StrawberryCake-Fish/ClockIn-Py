import configparser


class ParserToDict(configparser.ConfigParser):
    def dict(self):
        conf = dict(self._sections)
        for k in conf:
            conf[k] = dict(conf[k])
        return conf
