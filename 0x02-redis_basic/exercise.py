#!/usr/bin/env python3
"""writing string to Redis"""

import redis
import uuid
from typing import Union, Optional, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number ot times a method is called
    Args:
        method (callable): method to be decorated
    Returns:
        Callable: decorated method
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper to count the number of
        times a method is called"""
        random_key = method.__qualname__
        self._redis.incr(random_key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the number of time a method is called
    """
    random_key = method.__qualname__
    inputs = random_key + ":inputs"
    outputs = random_key + ":outputs"

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper to store the number of time a method is called
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def replay(method: Callable) -> None:
    """
    Decorator to replay the history of calls to
    a particular function
    """
    random_key = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(random_key).decode('utf-8')
    print("{} was called {} times:".format(random_key, calls))
    inputs = cache.lrange(random_key + ":inputs", 0, -1)
    outputs = cache.lrange(random_key + ":outputs", 0, -1)
    for inn, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     inn.decode('utf-8'),
                                     out.decode('utf-8')))


class Cache:
    """Cache classs"""

    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store method that takes a data
         argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """Get method that takes a key string argument
         and an optional Callable argument named fn"""
        original_data = self._redis.get(key)
        if fn:
            return fn(original_data)
        return original_data

    def get_str(self, key: str) -> str:
        """Automatically parameterize the get method"""
        original_data = self._redis.get(key)
        original_data.decode('utf-8')
        return original_data

    def get_int(self, key: str) -> int:
        """Automatically parameterize the get method to integer"""
        original_data = self._redis.get(key)
        return original_data.decode('utf-8')
