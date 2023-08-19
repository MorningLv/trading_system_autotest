# @Time: 2023/8/19 10:51
# @Author: LCC

class LeftMenuBase:
    def level_one_menu(self, menu_name):
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"


if __name__ == '__main__':
    print(LeftMenuBase().level_two_menu("我的商品列表"))
