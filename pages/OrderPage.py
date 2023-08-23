# @Time: 2023/8/20 20:56
# @Author: LCC
from selenium.webdriver.common.by import By

from base.OrderBase import OrderBase
from base.ObjectMap import ObjectMap

from logs.log import log


class OrderPage(OrderBase, ObjectMap):
    def click_order_tab(self, driver, tab_name):
        tab_xpath = self.order_tab(tab_name)
        return self.element_click(driver, By.XPATH, tab_xpath)

    def click_order_operation(self, driver, product_title, operation):
        log.info("订单标题为：" + product_title + ",点击订单的操作：" + operation)
        button_xpath = self.order_operation(product_title, operation)
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_order_operation_confirm(self, driver):
        log.info("点击订单操作按钮后的弹框的确认按钮")
        button_xpath = self.order_operation_confirm()
        return self.element_click(driver, By.XPATH, button_xpath)

    def click_delivery_logistics(self, driver):
        log.info("点击物流")
        input_xpath = self.delivery_logistics()
        return self.element_click(driver, By.XPATH, input_xpath)

    def click_select_logistitcs(self, driver, company):
        log.info("选择物流公司")
        select_xpath = self.select_logistics(company)
        return self.element_click(driver, By.XPATH, select_xpath)

    def input_logistics_order_no(self, driver, order_no):
        log.info("填写物流单号")
        input_xpath = self.logistics_order_no()
        return self.element_fill_value(driver, By.XPATH, input_xpath, order_no)
