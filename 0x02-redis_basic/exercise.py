#!/usr/bin/env python3
"""This module contains the class `Cache`.
"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    This is a function that returns a wrapper which increments a counter
    for a given key.
    The key is gotten from the qualified name of the `method` argument.
    The wrapper returns the original return value of the `redis.get` method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return self._redis.get(key)
    return wrapper


class Cache:
    """
    This is the Cache class.
    """

    def __init__(self):
        """
        This function runs when a new instance of the class is created.
        It gets the redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store generates a new key and stores `data` in redis using the key.
        It returns the key for the data.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        get returns the value of a given key converted to a specific type using
        the function `fn` if present. It otherwise return the value as is.
        """
        value = self._redis.get(key)
        return fn(value) if fn and value else value

    def get_str(self, key: str) -> Optional[str]:
        """
        get_str automatically parametizes `get` method with the correct func,
        in this case, `str`. It consequently returns a string.
        """
        return self.get(key, fn=lambda v: v.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        get_int automatically parametizes `get` method with the correct func,
        in this case, `int`. It consequently returns an int.
        """
        return self.get(key, fn=int)
