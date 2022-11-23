__all__ = ["Database", "Convertor", "Cursor"]

import sqlite3
from ProjectABC import ABClass
import constants

from typing import Iterable
from enum import Enum


class Database(ABClass):
    def __init__(self, config_path: str):
        super().__init__(config_path=config_path)
        self.connection = sqlite3.connect(self.config["database"]["name"], timeout=self.config["database"]["timeout"])
        self.cursor = Cursor(self.connection, self.config)

    select = self.cursor.select
    insert = self.cursor.insert
    update = self.cursor.update
    delete = self.cursor.delete
    drop = self.cursor.drop
    create = self.cursor.create
    execute = self.cursor.execute


class Cursor(ABClass):
    def __init__(self, connection: sqlite3.Connection, config: dict):
        super().__init__(config=config)
        self.connection = connection
        self.cursor = self.connection.cursor()

    def select(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def drop(self):
        pass

    def create(self):
        pass

    def execute(self, query: str, *attrs, convert: bool = True, output: constants.OutputType | None = None):
        exception = None
        for _ in range(self.config["database"]["attempts"]):
            try:
                self.cursor.execute(query, *attrs)
                if output == constants.OutputType.BOOL:
                    return True
                elif output == constants.OutputType.LIST:
                    return list(self.cursor)
                else:
                    return self.converter.convert_list(self.cursor)
            except Exception as e:
                exception = e
        
        if not isinstance(output, bool):
            raise exception
        print(exception)
        return False


class Converter:
    @staticmethod
    def convert_to(data: Iterable):
        pass

    @staticmethod
    def convert_from(data: Iterable):
        pass

    @staticmethod
    def convert_list(data: Iterable):
        try:
            if len(data) != 1:
                return data
            if isinstance(data[0], Iterable) and len(data[0]) == 1:
                return data[0][0]
            else:
                return data[0]
        except (IndexError, KeyError):
            return data
