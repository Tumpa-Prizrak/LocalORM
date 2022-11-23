from typing import Iterable, Any
import json


class ABClass:
    def __init__(self, config: dict = None, config_path: str = None):  # TODO add defaults
        if config is not None:
            self.config = config
        elif config_path is not None:
            self.config = json.load(open(config_path))
        else:
            raise ValueError("You must specify either config or config_path")

    def get_config(self):
        return str(self.config)

    def get_config_item(self, item: Iterable):
        x = self.config
        for i in item:
            x = x[i]
        return x

    def set_config_item(self, item: Iterable, value: Any):
        x = self.config
        for i in item:
            x = x[i]
        x = value
        self.config = x


class User:
    def __init__(self, id: int, username: str, password: str):
        self.id = id
        self.username = username
        self.password = password
