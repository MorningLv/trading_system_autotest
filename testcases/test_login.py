# @Time: 2023/8/18 17:36
# @Author: LCC

from time import sleep

from config.driver_config import DriverConfig
from pages.LoginPage import LoginPage


class TestLogin:
    def test_login(self):
        driver = DriverConfig().driver_config()
        driver.get("http://1.15.106.34")
        sleep(3)
        LoginPage().login_input_value(driver, "用户名", "周杰伦")
        LoginPage().login_input_value(driver, "密码", "123456")
        LoginPage().click_login(driver, "登录")
        sleep(3)
        driver.quit()
