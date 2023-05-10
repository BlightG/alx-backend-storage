#!/usr/bin/env python3
""" a moudle for the class Cache """
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ a class to cahce input """

    def __init__(self):
        """ initilaizes a new instance of the Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a method that takes a data argument and returns a string. """
        id = f'{uuid.uuid4()}'
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn=None:Callable[[Union[float, int, str]] int | str] ) -> Union[int, float, bytes, str]:
        """ a get method """
        print(f'fn = {fn}')
        if fn == str:
            return self.get_str(self._redis.get(key))
        if fn == int or fn == float:
            return self.get_int(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data):
        """ a get_str method """
        return str(data)

    def get_int(self, data):
        """ a get_int method """
        return int(data)

