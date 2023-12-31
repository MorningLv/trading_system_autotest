# @Time: 2023/8/18 17:29
# @Author: LCC
from selenium.webdriver.common.by import By
import requests
import time

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from logs.log import log


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        # 使用继承自LoginBase的login_input()来获取输入框的元素定位路径
        log.info("输入" + input_placeholder + "为：" + str(input_value))
        input_xpath = self.login_input(input_placeholder)
        # 使用driver查找元素并发送内容
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        log.info("点击登录")
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user):
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
        self.assert_login_success(driver)

    def api_login(self, driver, user):
        log.info("跳转登录页")
        self.element_to_url(driver, "/login")
        username, password = GetConf().get_username_password(user)
        log.info("用户名：" + str(username))
        log.info("密码：" + str(password))
        url = GetConf().get_url()
        data = {
            "user": username,
            "password": password
        }
        log.info("通过api登录")
        res = requests.post(url + "/api/user/login", json=data)
        token = res.json()["data"]["token"]
        js_script = "window.sessionStorage.setItem('token','%s');" % token
        log.info("将token写入sessionStorage")
        driver.execute_script(js_script)
        time.sleep(2)
        log.info("跳转主页")
        self.element_to_url(driver, "/")

    def assert_login_success(self, driver):
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath, timeout=2)
