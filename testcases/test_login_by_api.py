# @Time: 2023/8/23 14:45
# @Author: LCC
from time import sleep
import allure

from pages.LoginPage import LoginPage


class TestLoginByApi:
    def test_login_by_api(self, driver):
        with allure.step("登录jay"):
            LoginPage().api_login(driver, "jay")
            sleep(5)
        with allure.step("切换用户到William"):
            LoginPage().api_login(driver, "william")
            sleep(5)
