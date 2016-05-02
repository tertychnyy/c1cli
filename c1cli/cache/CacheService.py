import redis


class CacheService:

    def __init__(self, host, port, passwd, db=0, ssl=True):
        self.r = redis.StrictRedis(host=host, port=port, db=db, password=passwd, ssl=ssl)

    def ping(self):
        # Ping cache server
        return self.r.ping()

    def get(self, key):
        # Get value by key from cache
        return self.r.get(key)

    def set(self, key, value):
        # Save value to cache
        return self.r.set(key, value)

    def delete(self, key):
        # Save value to cache
        return self.r.delete(key)