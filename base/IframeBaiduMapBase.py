# @Time: 2023/8/21 10:04
# @Author: LCC
class IframeBaiduMapBase:
    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
