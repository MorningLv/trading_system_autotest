# @Time: 2023/8/18 17:36
# @Author: LCC

from time import sleep

import allure
import pytest

from pages.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLogin:
    def test_login(self, driver):
        LoginPage().login(driver, "jay")
        # driver.get("http://1.15.106.34")
        # sleep(3)
        # LoginPage().login_input_value(driver, "用户名", "周杰伦")
        # LoginPage().login_input_value(driver, "密码", "123456")
        # LoginPage().click_login(driver, "登录")
        sleep(3)

    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login_fail(self, driver):
        """使用错误的账号登录"""
        with allure.step("登录"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver, "登录")
