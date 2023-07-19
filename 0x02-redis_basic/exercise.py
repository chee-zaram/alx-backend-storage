#!/usr/bin/env python3
"""This module contains the class `Cache`.
"""
import redis
from typing import Union
from uuid import uuid4


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store generates a new key and stores `data` in redis using the key.
        It returns the key for the data.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
