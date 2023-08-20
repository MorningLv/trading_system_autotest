# @Time: 2023/8/20 20:39
# @Author: LCC
from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):
    def goto_imooc(self, driver):
        self.switch_win_to_lastest_handle(driver)
        return driver.title
