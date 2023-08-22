# @Time: 2023/8/20 16:44
# @Author: LCC
from time import sleep

import pytest

from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage
from pages.GoodsPage import GoodsPage

goods_info_list = [
    {
        "goods_title": "新增商品标题测试1",
        "goods_detail": "新增商品详情测试1",
        "goods_num": 3,
        "goods_pic_list": ["商品图片一.jpg"],
        "goods_price": 123,
        "goods_status": "上架",
        "button_name": "提交"
    },
    {
        "goods_title": "新增商品标题测试2",
        "goods_detail": "新增商品详情测试2",
        "goods_num": 2,
        "goods_pic_list": ["商品图片一.jpg"],
        "goods_price": 321,
        "goods_status": "上架",
        "button_name": "提交"
    }
]


class TestAddGoods:
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info["goods_title"],
            goods_detail=goods_info["goods_detail"],
            goods_num=goods_info["goods_num"],
            goods_pic_list=["商品图片一.jpg"],
            goods_price=goods_info["goods_price"],
            goods_status=goods_info["goods_status"],
            button_name=goods_info["button_name"]
        )
        sleep(3)
