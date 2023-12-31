# @Time: 2023/8/22 11:09
# @Author: LCC
import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
from common.process_redis import Process


def pytest_collection_finish(session):
    total = len(session.items)
    Process().reset_all()
    Process().init_process(total)


@pytest.fixture()
def driver():
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)

    if report.when == "call":
        if report.failed:
            add_img_2_report(get_driver, "失败截图", need_sleep=False)

            Process().update_fail()
            Process().insert_into_fail_testcase_names(report.description)

        elif report.passed:
            Process().update_success()

        else:
            pass
        process = Process().get_process()
        print(process)
