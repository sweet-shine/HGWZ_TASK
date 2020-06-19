import yaml

from UIAutoFrame.second_task.page.base import BasePage
from UIAutoFrame.second_task.page.market import Market_Page


class Main_Page(BasePage):

    def goto_market(self):
        self.set_implicitly_wait(10)
        with open("../page/main.yaml", encoding='utf-8') as f:
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
        # self.find_ele(MobileBy.XPATH, "//android.widget.TabHost//*[@text='行情']").click()
        self.set_implicitly_wait(5)
        return Market_Page(self._driver)
