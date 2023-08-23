# @Time: 2023/8/23 16:00
# @Author: LCC

from time import sleep
import pytest
import allure

from common.report_add_img import add_img_2_report
from common.tools import get_now_date_time_str
from pages.GoodsPage import GoodsPage
from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage


class TestTradingFlow:
    def test_trading_flow(self, driver):
        with allure.step("登录卖家"):
            LoginPage().api_login(driver, "jay")
            add_img_2_report(driver, "登录卖家")

        with allure.step("进入新增二手商品"):
            LeftMenuPage().click_level_one_menu(driver, "产品")
            sleep(3)
            LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
            add_img_2_report(driver, "进入新增二手商品")

        with allure.step("新增商品"):
            goods_title = "交易流测试" + get_now_date_time_str()
            GoodsPage().add_new_goods(
                driver,
                goods_title=goods_title,
                goods_detail="交易流测试",
                goods_num=3,
                goods_pic_list=["商品图片一.jpg"],
                goods_price=123,
                goods_status="上架",
                button_name="提交"
            )
            add_img_2_report(driver, "新增商品")
            sleep(3)
