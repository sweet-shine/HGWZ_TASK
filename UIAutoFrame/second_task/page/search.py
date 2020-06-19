import yaml
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.second_task.page.base import BasePage


class Search_Page(BasePage):
    # 搜索指定内容
    def search(self, func_name):
        with open('../page/search.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)[func_name]
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

    # 点击加自选
    def add(self, func_name):
        with open('../page/search.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)[func_name]
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

    # 判断是否已添加自选，查询text属性是已添加的元素
    def is_choose(self, func_name):
        with open('../page/search.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)[func_name]
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

    # 如果已添加自选，恢复为未添加自选
    def reset(self, func_name):
        with open('../page/search.yaml', encoding='utf-8') as f:
            steps = yaml.safe_load(f)[func_name]
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
