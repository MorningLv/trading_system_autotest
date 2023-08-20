# @Time: 2023/8/19 16:51
# @Author: LCC

class GoodsBase:
    def goods_title(self):
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品标题']"

    def goods_detail(self):
        return "//form[@class='el-form']//textarea[@placeholder='请输入商品详情']"

    def goods_num(self, plus=True):
        if plus:
            return "//label[@for='product_stock']/following-sibling::div//i[@class='el-icon-plus']/parent::span"
        else:
            return "//label[@for='product_stock']/following-sibling::div//input[@placeholder='商品数量']"

    def goods_img(self):
        return "//input[@type='file']"

    def goods_price(self):
        return "//form[@class='el-form']//input[@placeholder='请输入商品单价']"

    def goods_status(self):
        return "//form[@class='el-form']//input[@placeholder='请选择商品状态']"

    def goods_status_select(self, select_name):
        return "//span[text()='" + select_name + "']/parent::li"

    def goods_bottom_button(self, button_name):
        return "//span[text()='" + button_name + "']/parent::button"
