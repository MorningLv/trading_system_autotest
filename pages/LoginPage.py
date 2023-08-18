# @Time: 2023/8/18 17:29
# @Author: LCC
from base.LoginBase import LoginBase


class LoginPage(LoginBase):
    def login_input_value(self, driver, input_placeholder, input_value):
        # 使用继承自LoginBase的login_input()来获取输入框的元素定位路径
        input_xpath = self.login_input(input_placeholder)
        # 使用driver查找元素并发送内容
        return driver.find_element_by_xpath(input_xpath).send_keys(input_value)

    def click_login(self, driver, button_name):
        button_xpath = self.login_button(button_name)
        return driver.find_element_by_xpath(button_xpath).click()
