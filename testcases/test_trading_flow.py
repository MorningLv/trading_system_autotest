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
from pages.TradingMarketPage import TradingMarketPage
from pages.OrderPage import OrderPage


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

        with allure.step("登录买家"):
            LoginPage().api_login(driver, "william")
            add_img_2_report(driver, "登录买家")

        with allure.step("进入交易市场"):
            LeftMenuPage().click_level_one_menu(driver, "交易市场")
            add_img_2_report(driver, "进入交易市场")

        with allure.step("搜索宝贝"):
            TradingMarketPage().input_search_input(driver, goods_title)
            TradingMarketPage().click_search(driver)
            add_img_2_report(driver, "搜索宝贝")

        with allure.step("点击商品卡片"):
            TradingMarketPage().click_product_card(driver, goods_title)
            sleep(1)
            add_img_2_report(driver, "点击商品卡片")

        with allure.step("点击我想要"):
            TradingMarketPage().click_i_want(driver)
            sleep(1)
            add_img_2_report(driver, "点击我想要")

        with allure.step("选择详细收获地址"):
            TradingMarketPage().click_address(driver)
            sleep(1)
            TradingMarketPage().select_detail_address(driver, 1)
            sleep(1)
            add_img_2_report(driver, "选择第1个收获地址")

        with allure.step("点击确定按钮"):
            TradingMarketPage().click_bottom_buttom(driver)
            sleep(1)
            add_img_2_report(driver, "点击确定按钮")

        with allure.step("买家支付"):
            OrderPage().click_order_operation(driver, goods_title, "去支付")
            sleep(1)
            OrderPage().click_order_operation_confirm(driver)
            add_img_2_report(driver, "买家支付")
