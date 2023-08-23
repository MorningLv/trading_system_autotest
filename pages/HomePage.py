# @Time: 2023/8/23 15:26
# @Author: LCC
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.HomeBase import HomeBase


class HomePage(HomeBase, ObjectMap):
    def get_balance(self, driver):
        balance_xpath = self.user_balance()
        return self.element_get(driver, By.XPATH, balance_xpath).text
