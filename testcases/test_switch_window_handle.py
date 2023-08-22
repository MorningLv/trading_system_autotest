# @Time: 2023/8/20 20:41
# @Author: LCC
from time import sleep
import allure

from pages.ExternalLinkPage import ExternalLinkPage
from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage

from common.report_add_img import add_img_2_report


class TestWindowHandle:
    @allure.description("窗口句柄")
    def test_switch_window_handles(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(1)

        with allure.step("断言title"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("title:" + title)
            assert "慕课网" in title
