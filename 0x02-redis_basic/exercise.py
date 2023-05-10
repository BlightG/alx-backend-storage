#!/usr/bin/env python3
""" a moudle for the class Cache """
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


class Cache:
    """ a class to cahce input """

    def __init__(self):
        """ initilaizes a new instance of the Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """ wrapper """
        key = method.__qualname__

        @wraps(method)
        def wrapper(*args, **kwargs):
            """ wraped """
            self = args[0]
            self._redis.incr(key)
            return method(*args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a method that takes a data argument and returns a string. """
        id = f'{uuid.uuid4()}'
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable[[Union[str, bytes]], Union[str, bytes, int, float]]] = None) -> Union[str, bytes, int, float]:
        """ a get method """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, data):
        """ a get_str method """
        return self.get(data, str)

    def get_int(self, data):
        """ a get_int method """
        return self.get(data, int)

