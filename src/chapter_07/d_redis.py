import redis


def test():
    r = redis.Redis(host="localhost", port=6379, password=None)
    r.set("key", "value")
    v = r.get("key")
    print(v)  # виведе b'value'

# =========================

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

@cache
def f(x):
    print(f"Function call f({x})")
    return x


def test_lru():
    print(f"Result f(3): {f(3)}")
    print(f"Result f(3): {f(3)}")



if __name__ == "__main__":
    test()
    test_lru()
