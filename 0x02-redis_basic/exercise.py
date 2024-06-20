#!/usr/bin/env python3
"""writing string to Redis"""

import redis
import uuid
from typing import Union


class Cache:
    """Cache classs"""

    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data
         argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
