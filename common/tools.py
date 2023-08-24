# @Time: 2023/8/18 15:22
# @Author: LCC
import os
import time


def get_project_path():  # 获取项目绝对路径
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):  # 给路径添加分隔符
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_img_path(img_name):
    img_path = get_project_path() + sep(["img", img_name], add_sep_before=True)
    return img_path


def get_now_date_time_str():
    return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


if __name__ == '__main__':
    print(get_now_time())
