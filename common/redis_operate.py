# @Time: 2023/8/23 23:20
# @Author: LCC

import redis

from common.yaml_config import GetConf


class RedisOperate:
    def __init__(self):
        redis_info = GetConf().get_redis_config()
        self.redis_client = redis.Redis(
            host=redis_info["host"],
            port=redis_info["port"],
            db=redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding="UTF-8"
            # password=user:password
        )


if __name__ == '__main__':
    print(RedisOperate().redis_client.get("william"))
