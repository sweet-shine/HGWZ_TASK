# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.base import BasePage
from APP.second_task.page.contracts import ContractsPage


class MainPage(BasePage):

    def goto_contracts(self):
        self.find_ele(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContractsPage(self._driver)
