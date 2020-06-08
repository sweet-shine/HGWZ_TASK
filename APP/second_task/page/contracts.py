# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.addmember import AddMemberPage
from APP.second_task.page.base import BasePage
from APP.second_task.page.delmember import DelMemberPage


class ContractsPage(BasePage):

    def goto_addmember(self):
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='添加成员']").click()
        return AddMemberPage(self._driver)

    def get_members_num(self):
        members = self.find_eles(MobileBy.XPATH, '//android.widget.ListView/android.widget.RelativeLayout')
        num = len(members)-2
        return num

    def goto_delmember(self):
        return DelMemberPage(self._driver)

