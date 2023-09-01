# 框架介绍

Selenium+Requests+pytest框架作为控制层进行逻辑验证，YAML作为持久层进行测试数据的存储，利用Logging 埋点记录日志，使用Allure展示测试报告

![](https://cdn.staticaly.com/gh/MorningLv/picx-images-hosting@master/img/202309011524290.png)

# 目录介绍

base: 包括对selenium操作进行二次封装的ObjectMap模块，以及对各个页面元素的封装模块

common: 包括对MySQL、Redis、添加报告截图、获取yaml文件配置、以及其他通用方法

config: 包括driver方法、配置信息的yaml文件

driver_files：存放浏览器驱动

img: 存放页面用到的图片

logs: 日志相关

page: 页面类，对页面元素的操作

testcase: 测试用例
