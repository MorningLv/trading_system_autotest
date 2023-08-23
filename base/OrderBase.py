# @Time: 2023/8/20 20:55
# @Author: LCC

class OrderBase:
    def order_tab(self, tab_name):
        return "//div[@role='tab' and text()='" + tab_name + "']"

    def order_operation(self, product_title, operation):
        return "//div[text()='" + product_title + "']/ancestor::tr//span[text()='" + operation + "']/parent::button"

    def order_operation_confirm(self):
        return "//div[@class='el-dialog__wrapper' and contains(@style,'index')]//span[text()='确 定']/parent::button"

    def delivery_logistics(self):
        return "//label[text()='物流公司']/following-sibling::div//input"

    def select_logistics(self, company):
        return "//span[text()='" + company + "']/parent::li"

    def logistics_order_no(self):
        return "//label[text()='物流单号']/following-sibling::div//input"

    def evaluation(self, num):
        return "//span[text()='请给卖家评价']/following-sibling::div/span[" + str(num) + "]/i"

    def evaluation_confirm(self):
        return "//span[text()='评价']/ancestor::div[@role='dialog']//span[text()='确 定']/parent::button"
