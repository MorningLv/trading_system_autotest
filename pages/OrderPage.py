# @Time: 2023/8/20 20:56
# @Author: LCC
from selenium.webdriver.common.by import By

from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap


class OrderPage(OrderBase, ObjectMap):
    def click_order_tab(self, driver, tab_name):
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)