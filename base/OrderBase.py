# @Time: 2023/8/20 20:55
# @Author: LCC

class OrderBase:
    def order_tab(self, tab_name):
        return "//div[@role='tab' and text()='" + tab_name + "']"

    def order_operation(self, product_title, operation):
        return "//div[text()='" + product_title + "']/ancestor::tr//span[text()='" + operation + "']/parent::button"

    def order_operation_confirm(self):
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确定']/parent::button"
