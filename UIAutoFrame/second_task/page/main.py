import yaml

from UIAutoFrame.second_task.page.base import BasePage
from UIAutoFrame.second_task.page.market import Market_Page


class Main_Page(BasePage):

    def goto_market(self):
        self.set_implicitly_wait(10)
        self.steps("../page/main.yaml")
        self.set_implicitly_wait(5)
        return Market_Page(self._driver)
