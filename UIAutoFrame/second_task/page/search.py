import time

import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.second_task.page.base import BasePage


class Search_Page(BasePage):
    # 搜索指定内容
    def search(self):
        self.steps('../page/search.yaml')
        time.sleep(1.5)
        return self

    # 点击加自选
    def add(self):
        self.steps('../page/search.yaml')
        return self

    # 判断是否已添加自选，查询text属性是已添加的元素
    def is_choose(self):
        self.steps('../page/search.yaml')
        return self

    # 如果已添加自选，恢复为未添加自选
    def reset(self):
        self.steps('../page/search.yaml')
        return self
