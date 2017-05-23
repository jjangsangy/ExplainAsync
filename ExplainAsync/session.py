# -*- coding: utf-8 -*-
import asyncio_redis
from sanic_session import RedisSessionInterface

class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None
    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host='localhost',
                port=6379,
                poolsize=10)
        return self._pool

def create_session():
    redis = Redis()
    return RedisSessionInterface(redis.get_redis_pool)
