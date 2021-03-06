# -*- coding: utf-8 -*-

from pyutil.springdb.client import ClientBase

class RedisClient(ClientBase):
    '''
    This client is designed to be compatible with SpringDBClient, in order to
    switch backend between springdb and redis.

    Construction is not cost-free, you should avoid constructing it too
    frequently. Moreover, it's thread-safe.
    '''

    # constants
    CLIENT_NAME = 'RedisClient'
    METRIC_PREFIX = 'inf.redisclient' # metric prefix
    SUPPORTED_COMMANDS = [
        'exists', 'expire', 'expireat', 'persist', 'move',
        'del', 'rename', 'renamenx',

        'set', 'setnx', 'setex', 'psetex', 'getset', 'setbit', 'setrange',
        'incr', 'decr', 'incrby', 'decrby', 'incrbyfloat', 'mset', 'msetnx',
        'get', 'exists', 'bitcount', 'getbit', 'getrange', 'strlen', 'mget',

        'sadd', 'srem', 'smove', 'brpoplpush',
        'scard', 'sismember', 'smembers', 'srandmember',
        'sdiff', 'sinter', 'sunion' 'sdiffstore', 'sinterstore', 'sunionstore',

        'hset', 'hmset', 'hdel', 'hincrby', 'hincrbyfloat',
        'hget', 'hmget', 'hexists', 'hlen', 'hgetall', 'hkeys', 'hvals',

        'zadd', 'zincrby', 'zrem', 'zremrangebyrank', 'zremrangebyscore',
        'zremrangebylex',
        'zcard', 'zcount', 'zlexcount', 'zscore', 'zrank', 'zrevrank',
        'zrange', 'zrangebyscore', 'zrevrange', 'zrevrangebyscore',

        'lpush', 'lpushx', 'rpush', 'rpushx', 'lpop', 'rpop', 'linsert', 'lset',
        'ltrim', 'blpop', 'brpop',
        'llen', 'lindex', 'lrange',

        'pfadd', 'pfmerge', 'pfcount',

        'sort', 'append',

        'auth', 'flushall', 'flushdb', 'save', 'select', 'shutdown', 'slaveof',
        'bgrewriteaof', 'bgsave', 'watch', 'unwatch',
    ]

    # static data
    _zone = 'auto'

    @staticmethod
    def set_zone(zone):
        '''
        use /etc/ss_conf as default conf directory

        @param zone: auto/online/offline/test
        '''
        RedisClient._zone = zone

    def __init__(self, *args, **kwargs):
        '''
        @param string cluster, the cluster name
        @param string table, the table name which will add as prefix in the key
        @param socket_timeout in seconds
        @param socket_connect_timeout in seconds

        example:
            db = RedisClient('redis_sandbox', 'sandbox', 0.25, 0.1)

        Please do not pass in a server list as cluster, use the cluster name
        instead.
        '''
        kwargs['module'] = 'redis'
        kwargs['zone'] = RedisClient._zone
        ClientBase.__init__(self, *args, **kwargs)

if __name__ == '__main__':
    import logging
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    logging.getLogger().setLevel(logging.DEBUG)

    RedisClient.set_zone('online')
    c = RedisClient('redis_sandbox', 'sandbox')
    key = '12:1592632028:16254'
    print 'key:', key
    print 'result:', c.set(key, 'abc')

