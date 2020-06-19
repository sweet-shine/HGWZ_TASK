import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.second_task.page.base import BasePage
from UIAutoFrame.second_task.page.search import Search_Page


class Market_Page(BasePage):

    def goto_search(self):
        with open('../page/market.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find_ele(step["by"], step["locator"])
                    if "action" in step.keys():
                        action = step["action"]
                        if "click" == action:
                            element.click()
                        elif "send" == action:
                            element.send_keys(step["value"])
        return Search_Page(self._driver)
