import redis

redis_config_example = {
    'host': '127.0.0.1',
    'port': '6379',
    'db': 4,
    'auth': True,
    'charset': 'utf-8',
    'password': ''
}

def cache_conn(redis_config={}):
    if not redis_config:
        redis_config = redis_config_example
    auth = redis_config.get('auth')
    db = redis_config.get('db')
    host = redis_config.get('host')
    port = redis_config.get('port')
    password = redis_config.get('password')
    charset = redis_config.get('charset')
    if auth:
        redis_pool = redis.ConnectionPool(host=host, port=port, db=db, password=password,
                                          decode_responses=charset)
    else:
        redis_pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=charset)
    cache_conns = redis.StrictRedis(connection_pool=redis_pool)
    return cache_conns

if __name__ == '__main__':
    redis_config = {
        'host': '127.0.0.1',
        'port': '6379',
        'db': 4,
        'auth': True,
        'charset': 'utf-8',
        'password': ''
    }
    redis_conn = cache_conn(redis_config)
    redis_conn.sadd('test01','002')