import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.second_task.page.base import BasePage


class Search_Page(BasePage):
    def search(self):
        with open('../page/search1.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find_ele(step["by"], step["locator"])
                    if "action" in step.keys():
                        action = step["action"]
                        if "click" == action:
                            element.click()
                        elif "send_keys" == action:
                            element.send_keys(step["value"])
                elif "bys" in step.keys():
                    elements = self.find_ele(step["bys"], step["locator"])
                    if "action" in step.keys() and "click" in step.keys():
                        elements[step["index"]].click()
                    elif "action" in step.keys() and "len" in step.keys():
                        return len(elements)
        return self

    def add(self):
        with open('../page/search2.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find_ele(step["by"], step["locator"])
                    if "action" in step.keys():
                        action = step["action"]
                        if "click" == action:
                            element.click()
                        elif "send_keys" == action:
                            element.send_keys(step["value"])
                elif "bys" in step.keys():
                    elements = self.find_ele(step["bys"], step["locator"])
                    if "action" in step.keys() and "click" in step.keys():
                        elements[step["index"]].click()
                    elif "action" in step.keys() and "len" in step.keys():
                        return len(elements)
        return self

    def is_choose(self):
        with open('../page/search3.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find_ele(step["by"], step["locator"])
                    if "action" in step.keys():
                        action = step["action"]
                        if "click" == action:
                            element.click()
                        elif "send_keys" == action:
                            element.send_keys(step["value"])
                elif "bys" in step.keys():
                    elements = self.find_eles(step["bys"], step["locator"])
                    if "action" in step.keys() and "click" in step.keys():
                        elements[step["index"]].click()
                    elif "action" in step.keys() and "len" in step.keys():
                        return len(elements)
        return self

    def reset(self):
        with open('../page/search4.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find_ele(step["by"], step["locator"])
                    if "action" in step.keys():
                        action = step["action"]
                        if "click" == action:
                            element.click()
                        elif "send_keys" == action:
                            element.send_keys(step["value"])
                elif "bys" in step.keys():
                    elements = self.find_eles(step["bys"], step["locator"])
                    if "action" in step.keys() and "click" in step.values():
                        elements[step["index"]].click()
                    elif "action" in step.keys() and "len" in step.values():
                        return len(elements)
        return self
