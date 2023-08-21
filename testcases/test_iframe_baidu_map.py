# @Time: 2023/8/21 10:08
# @Author: LCC
from time import sleep

from config.driver_config import DriverConfig
from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage

from pages.IframeBaiduMapPage import IframeBaiduMapPage


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)

        IframeBaiduMapPage().switch_to_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")

        sleep(3)
        driver.quit()
