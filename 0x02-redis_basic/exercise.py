#!/usr/bin/env python3
""" a moudle for the class Cache """
import redis
import uuid
from typing import Union


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

