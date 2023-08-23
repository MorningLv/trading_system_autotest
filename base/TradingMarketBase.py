# @Time: 2023/8/23 16:32
# @Author: LCC
class TradingMarketBase:
    def search_input(self):
        return "//div[text()='搜索宝贝']/following-sibling::input"

    def search(self):
        return self.search_input() + "/following-sibling::div/button"

    def product_card(self, product_name):
        return "//div[text()='" + product_name + "']/ancestor::div[@class='el-card__body']"

    def i_want_button(self):
        return "//span[text()='我想要']/parent::button"

    def receive_address(self):
        return "//input[@placeholder='收货地址']"

    def receive_address_detail(self, num, address=None):
        if address:
            return "//span[text()='" + address + "']/parent::li"
        else:
            return "//ul[contains(@class,'list')]/li[" + str(num) + "]"

    def button_confirm(self):
        return "//span[text()='确 定']/parent::button"
