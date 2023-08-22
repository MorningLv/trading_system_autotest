# @Time: 2023/8/20 16:44
# @Author: LCC
from time import sleep

from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage
from pages.GoodsPage import GoodsPage


class TestAddGoods:
    def test_add_goods_001(self, driver):
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title="新增商品标题测试",
            goods_detail="新增商品详情测试",
            goods_num=3,
            goods_pic_list=["商品图片一.jpg"],
            goods_price=123,
            goods_status="上架",
            button_name="提交"
        )
        sleep(3)
