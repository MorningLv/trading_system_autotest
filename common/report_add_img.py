# @Time: 2023/8/22 17:01
# @Author: LCC
import allure
from time import sleep


def add_img_2_report(driver, step_name, need_sleep=True):
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)
