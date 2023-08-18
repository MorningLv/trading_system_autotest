# @Time: 2023/8/18 14:48
# @Author: LCC
import yaml


class GetConf:
    def __init__(self):
        with open("../config/environment.yaml", "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self):
        return self.env["username"], self.env["password"]


if __name__ == '__main__':
    print(GetConf().get_username_password())
