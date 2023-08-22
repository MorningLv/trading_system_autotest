# @Time: 2023/8/20 20:56
# @Author: LCC
from time import sleep

import pytest

from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage
from pages.OrderPage import OrderPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


@pytest.mark.parametrize("tab", tab_list)
class TestOrderBuyList:
    def test_add_goods_001(self, driver, tab):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        OrderPage().click_order_tab(driver, tab)
        sleep(3)
