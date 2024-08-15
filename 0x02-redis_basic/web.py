#!/usr/bin/python3

"""
created at Aug 15, 2024
@Author: James Gatheru
"""

from functools import wraps
import redis
import requests

redis_client = redis.Redis()


def count_requests(method):
    """
    Decorator for counting
    """
    @wraps(method)
    def wrapper(url):
        key_count = f"count:{url}"
        key_cached = f"cached:{url}"

        cached_value = redis_client.get(key_cached)
        if cached_value:
            return cached_value.decode('utf-8')

        hmtl_content = method(url)

        redis_client.incr(key_count)
        redis_client.setex(key_cached, 10, hmtl_content)

        return hmtl_content
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a URL
    """
    response = requests.get(url, timeout=10)
    return response.text


if __name__ == "__main__":
    URL = 'http://slowwly.robertomurray.co.ke'
    print(get_page(URL))
