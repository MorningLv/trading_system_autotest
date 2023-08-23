# @Time: 2023/8/22 23:40
# @Author: LCC
import logging
import os
import time

from common.tools import get_project_path, sep


def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    # 设置日志存放路径，日志文件名
    # 获取本地时间并格式化
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 设置日志存放路径
    all_log_path = get_project_path() + sep(["logs", "all_logs"], add_sep_before=True, add_sep_after=True)
    # 如果日志目录不存在则自动创建
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    # 设置日志文件名
    all_log_name = all_log_path + rq + ".log"
    # 创建Handler
    # 创建Handler写入日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    # 定义日志内容输出格式
    all_log_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")
    # 将定义好的输出格式添加到Handler
    fh.setFormatter(all_log_formatter)
    # 给创建的logger添加Handler
    logger.addHandler(fh)
    return logger


log = get_log("自动化测试")

if __name__ == '__main__':
    log.debug("debug message")
    log.info("info message")
    log.warning("warning message")
    log.error("error message")
    log.critical("critical message")
