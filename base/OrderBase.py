# @Time: 2023/8/20 20:55
# @Author: LCC

class OrderBase:
    def order_tab(self, tab_name):
        return "//div[@role='tab' and text()='" + tab_name + "']"
