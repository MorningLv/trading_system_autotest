# @Time: 2023/8/22 11:09
# @Author: LCC
import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
