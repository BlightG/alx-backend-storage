#!/usr/bin/env python3
""" a moudle for the class Cache """
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def replay(method: Callable):
    """ replays sequence of events """
    r = redis.Redis()
    func_name = method.__qualname__
    c = r.get(func_name)
    try:
        c = int(c.decode("utf-8"))
    except Exception:
        c = 0
    print("{} was called {} times:".format(func_name, c))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for inp, outp in zip(inputs, outputs):
        try:
            inp = inp.decode("utf-8")
        except Exception:
            inp = ""
        try:
            outp = outp.decode("utf-8")
        except Exception:
            outp = ""
        print("{}(*{}) -> {}".format(func_name, inp, outp))

class Cache:
    """ a class to cahce input """

    def __init__(self):
        """ initilaizes a new instance of the Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def call_history(method: Callable) -> Callable:
        """ input and output list """
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'

        @wraps(method)
        def wrapper(*args, **kwargs) -> Callable:
            """ returns a wraped function """
            self = args[0]
            self._redis.rpush(input_key, f"({args[1]},)")
            self._redis.rpush(output_key, method(self, args[1]))
            return method(*args, *kwargs)
        return wrapper

    def count_calls(method: Callable) -> Callable:
        """ wraps store and used to conut """
        key = method.__qualname__
        # print(key)

        @wraps(method)
        def wrapper(*args, **kwargs):
            """ wraped """
            self = args[0]
            self._redis.incr(key)
            return method(*args, **kwargs)
        return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ a method that takes a data argument and returns a string. """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable[[Union[str, bytes]],
            Union[str, bytes, int, float]]] = None)\
            -> Union[str, bytes, int, float]:
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
