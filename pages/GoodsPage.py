# @Time: 2023/8/20 16:04
# @Author: LCC
from selenium.webdriver.common.by import By
from time import sleep

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from common.tools import get_img_path


class GoodsPage(GoodsBase, ObjectMap):
    def input_goods_title(self, driver, input_value):
        goods_title_xpath = self.goods_title()
        return self.element_fill_value(driver, By.XPATH, goods_title_xpath, input_value)

    def input_goods_detail(self, driver, input_value):
        goods_detail_xpath = self.goods_detail()
        return self.element_fill_value(driver, By.XPATH, goods_detail_xpath, input_value)

    def input_goods_num(self, driver, num):
        goods_num_xpath = self.goods_num(plus=True)
        for i in range(num):
            self.element_click(driver, By.XPATH, goods_num_xpath)
            sleep(0.5)

    def upload_goods_img(self, driver, img_name):
        img_path = get_img_path(img_name)
        upload_xpath = self.goods_img()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def input_goods_price(self, driver, input_value):
        goods_price_xpath = self.goods_price()
        return self.element_fill_value(driver, By.XPATH, goods_price_xpath, input_value)

    def select_goods_status(self, driver, select_name):
        goods_status_xpath = self.goods_status()
        self.element_click(driver, By.XPATH, goods_status_xpath)
        sleep(1)
        goods_status_select_xpath = self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH, goods_status_select_xpath)

    def click_bottom_button(self, driver, button_name):
        button_xpath = self.goods_bottom_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def add_new_goods(self, driver, goods_title, goods_detail, goods_num, goods_pic_list, goods_price, goods_status,
                      button_name):
        self.input_goods_title(driver, goods_title)
        self.input_goods_detail(driver, goods_detail)
        self.input_goods_num(driver, goods_num)
        for goods_pic in goods_pic_list:
            self.upload_goods_img(driver, goods_pic)
            sleep(5)
        self.input_goods_price(driver, goods_price)
        self.select_goods_status(driver, goods_status)
        self.click_bottom_button(driver, button_name)
        return True
