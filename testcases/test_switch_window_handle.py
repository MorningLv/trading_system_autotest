# @Time: 2023/8/20 20:41
# @Author: LCC
from time import sleep
from config.driver_config import DriverConfig
from pages.ExternalLinkPage import ExternalLinkPage
from pages.LoginPage import LoginPage
from pages.LeftMenuPage import LeftMenuPage


class TestWindowHandle:
    def test_switch_window_handles(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(1)
        title = ExternalLinkPage().goto_imooc(driver)
        print("title:" + title)
        driver.quit()
