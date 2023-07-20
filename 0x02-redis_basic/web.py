#!/usr/bin/env python3
"""
This is the module `web`.
"""
import requests
import redis
from typing import Callable
from functools import wraps


# Module-level redis cache object.
cache = redis.Redis()


def count_requests(fn: Callable) -> Callable:
    """
    count_url returns a wrapper that counts the number of times
    a request is made to a url.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """
        wrapper creates a cache of the html content returned by the given url.
        """
        if type(url) != str:
            return ""

        cache.incr("count:{}".format(url))
        html = cache.get("{}".format(url))
        if html and type(html) == bytes:
            return html.decode("utf-8")

        html = fn(url)
        cache.setex("{}".format(url), 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    get_page obtains a HTML content of a URL and returns it.
    """
    if type(url) != str:
        return ""

    return requests.get(url).text
