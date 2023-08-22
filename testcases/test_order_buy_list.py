# @Time: 2023/8/20 20:56
# @Author: LCC
from time import sleep

from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage
from pages.OrderPage import OrderPage


class TestOrderBuyList:
    def test_add_goods_001(self, driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for tab in tab_list:
            OrderPage().click_order_tab(driver, tab_name=tab)
            sleep(0.5)
        sleep(3)
