# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.addmember import AddMemberPage
from APP.second_task.page.base import BasePage


class ContractsPage(BasePage):

    def goto_addmember(self):

        # //*[@resource-id='com.tencent.wework:id/drn'][last()]
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/drw'][last()]").click()
        return AddMemberPage(self._driver)