# @Time: 2023/8/23 16:48
# @Author: LCC
from time import sleep
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.TradingMarketBase import TradingMarketBase
from logs.log import log


class TradingMarketPage(TradingMarketBase, ObjectMap):
    def input_search_input(self, driver, input_value):
        log.info("搜索宝贝输入框输入" + input_value)
        search_input_xpath = self.search_input()
        return self.element_fill_value(driver, By.XPATH, search_input_xpath, input_value)

    def click_search(self, driver):
        log.info("点击搜索按钮")
        search_xpath = self.search()
        return self.element_click(driver, By.XPATH, search_xpath)

    def click_product_card(self, driver, product_name):
        log.info("点击商品卡片,商品名称为：" + product_name)
        product_card_xpath = self.product_card(product_name)
        return self.element_click(driver, By.XPATH, product_card_xpath)

    def click_i_want(self, driver):
        log.info("点击我想要")
        i_want_button_xpath = self.i_want_button()
        self.scroll_to_element(driver, By.XPATH, i_want_button_xpath)
        return self.element_click(driver, By.XPATH, i_want_button_xpath)

    def click_address(self, driver):
        log.info("点击收获地址")
        receive_xpath = self.receive_address()
        return self.element_click(driver, By.XPATH, receive_xpath)

    def select_detail_address(self, driver, num, address=None):
        if address:
            log.info("选择具体收获地址" + address)
            address_xpath = self.receive_address_detail(0, address=address)
        else:
            log.info("选择第" + str(num) + "个收获地址")
            address_xpath = self.receive_address_detail(num)
        return self.element_click(driver, By.XPATH, address_xpath)

    def click_bottom_buttom(self, driver):
        log.info("点击确定按钮")
        button_xpath = self.button_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)
