# @Time: 2023/8/18 15:22
# @Author: LCC
import os


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


if __name__ == '__main__':
    print(sep(["config", "environment.yaml"], add_sep_after=True, add_sep_before=True))
