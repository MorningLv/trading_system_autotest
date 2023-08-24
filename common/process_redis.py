# @Time: 2023/8/24 21:35
# @Author: LCC
from common.tools import get_now_time
from common.redis_operate import RedisOperate


class Process:
    def __init__(self):
        self.redis_client = RedisOperate().redis_client
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"
        self.FAILED_TESTCASES_NAMES = "failed_testcase_name"
        self.RUNNING_STATUS = "running_status"

    def reset_all(self):
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        self.redis_client.delete(self.FAILED_TESTCASES_NAMES)

    def init_process(self, total):
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", get_now_time())
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNING_STATUS, 1)

    def update_success(self):
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail")

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        self.redis_client.lpush(self.FAILED_TESTCASES_NAMES, fail_testcase_name)

    def get_result(self):
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0

        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0

        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0

        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = '-'

        return total, success, fail, start_time

    def get_process(self):
        total, success, fail, _ = self.get_result()
        if total == 0:
            return 0
        else:
            return "%.1f" % ((int(success) + int(fail)) / int(total) * 100) + "%"

    def get_fail_testcase_names(self):
        fail_testcase_names = self.redis_client.lrange(self.FAILED_TESTCASES_NAMES, 0, -1)
        return fail_testcase_names

    def write_end_time(self):
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", get_now_time())

    def modify_running_status(self, status):
        self.redis_client.set(self.RUNNING_STATUS, status)
