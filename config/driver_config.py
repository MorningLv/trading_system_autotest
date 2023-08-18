# @Time: 2023/8/18 14:02
# @Author: LCC

from selenium import webdriver

from common.tools import get_project_path, sep


class DriverConfig:
    def driver_config(self):
        options = webdriver.ChromeOptions()
        # 设置窗口大小
        options.add_argument("window-size-1920,1080")
        # 去除Chrome正收到自动测试软件控制的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certification-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incogito")
        # 设置无头模式
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            executable_path=get_project_path() + sep(["driver_files", "chromedriver.exe"], add_sep_before=True),
            options=options)
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
