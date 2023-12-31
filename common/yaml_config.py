# @Time: 2023/8/18 14:48
# @Author: LCC
import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis_config(self):
        return self.env["redis"]


if __name__ == '__main__':
    print(GetConf().get_redis_config())
