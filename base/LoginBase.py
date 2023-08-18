# @Time: 2023/8/18 16:59
# @Author: LCC

class LoginBase:
    def login_input(self, input_placeholder):
        # 传入元素定位名称input_placeholder，返回元素定位路径
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        return "//span[text()='" + button_name + "']/parent::button"


if __name__ == '__main__':
    print(LoginBase().login_button("登录"))
