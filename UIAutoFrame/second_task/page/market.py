import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.second_task.page.base import BasePage
from UIAutoFrame.second_task.page.search import Search_Page


class Market_Page(BasePage):

    def goto_search(self):
        self.steps('../page/market.yaml')
        return Search_Page(self._driver)
