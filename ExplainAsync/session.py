# -*- coding: utf-8 -*-
import asyncio_redis

from sanic_session import RedisSessionInterface, InMemorySessionInterface
from urllib.parse import urlparse

import os

class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    def __init__(self, host='127.0.0.1', port=6379, password=None, size=10):
        self.host = host
        self.port = port
        self.password = password
        self.size = size

    @classmethod
    def from_url(cls, url):
        url = urlparse(url)
        return cls(host=url.hostname, port=url.port, password=url.password)

    async def get_redis_pool(self) -> asyncio_redis.Pool:

        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host=self.host,
                port=self.port,
                password=self.password,
                poolsize=self.size)

        return self._pool


def get_session():
    redis_url = os.getenv('REDIS_URL')
    if redis_url:
        redis = Redis.from_url(url)
        return RedisSessionInterface(redis.get_redis_pool)
    else:
        return InMemorySessionInterface()
