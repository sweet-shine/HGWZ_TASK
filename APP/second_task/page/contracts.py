# coding=utf-8
# auther:wangc
# 2020-05-26
import re

from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.addmember import AddMemberPage
from APP.second_task.page.base import BasePage
from APP.second_task.page.delmember import DelMemberPage


class ContractsPage(BasePage):

    def goto_addmember(self):
        # self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='添加成员']").click()
        self.scroll_find('添加成员').click()
        return AddMemberPage(self._driver)

    def get_members_num(self):
        # members = self.find_eles(MobileBy.XPATH, '//android.widget.ListView/android.widget.RelativeLayout')
        # num = len(members)-2
        # return num
        text = self.scroll_find_start_text('共').text
        num = int(re.findall("共(\d*)人", text)[0])
        return num

    def goto_delmember(self):
        return DelMemberPage(self._driver)
