import json


class Utils:

    @staticmethod
    def load_json(file: str) -> dict:
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
        return data
