# @Time: 2023/8/21 10:06
# @Author: LCC
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IframeBaiduMapPage(IframeBaiduMapBase, ObjectMap):
    def get_baidu_map_search_button(self, driver):
        button_xpath = self.search_button()
        return self.element_click(driver, By.XPATH, button_xpath)

    def switch_to_baidu_map_iframe(self, driver):
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        return self.switch_from_ifame_to_content(driver)
