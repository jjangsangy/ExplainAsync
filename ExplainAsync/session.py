# -*- coding: utf-8 -*-
import asyncio_redis
from sanic_session import RedisSessionInterface
from urllib.parse import urlparse

import os

class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    @classmethod
    def from_url(cls, url, db=None, decode_components=False, **kwargs):
        url = urlparse(url)

        return cls(**kwargs)

    async def get_redis_pool(self):
        url = urlparse(os.getenv('REDIS_URL', 'redis://127.0.0.1:6379'))
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host=url.hostname,
                port=url.port,
                password=url.password,
                poolsize=10)
        return self._pool

def create_session():
    redis = Redis()
    return RedisSessionInterface(redis.get_redis_pool)
