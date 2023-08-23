# @Time: 2023/8/19 10:05
# @Author: LCC

class HomeBase:
    def wallet_switch(self):
        # 首页钱包开关
        return "//span[contains(@class,'switch')]"

    def logo(self):
        # 首页左上角logo
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        # 首页欢迎您回来
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_date(self):
        # 首页日历日期
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        # 首页用户头像
        # 方式一 ：//span[starts-with(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img
        # 方式二 ：//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'user_avatar')]//img
        return "//span[starts-with(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

    def user_balance(self):
        return "//th[text()='账户余额']/parent::tr/following-sibling::tr/td[1]"
