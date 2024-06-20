#!/usr/bin/env python3
"""writing string to Redis"""

import redis
import uuid
from typing import Union, Optional, Callable


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
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get method that takes a key string argument
         and an optional Callable argument named fn"""
        original_data = self._redis.get(key)
        if fn:
            return fn(original_data)
        return original_data
        
    def get_str(self, key: str ) -> str:
        """Automatically parameterize the get method"""
        original_data = self._redis.get(key)
        original_data.decode('utf-8')
        return original_data
    
    def get_int(self, key: str) -> int:
        """Automatically parameterize the get method to integer"""
        original_data = self._redis.get(key)
        return original_data.decode('utf-8')