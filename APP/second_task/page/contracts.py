# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.addmember import AddMemberPage
from APP.second_task.page.base import BasePage
from APP.second_task.page.p_info import PInfoPage


class ContractsPage(BasePage):

    def goto_addmember(self):
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b0_']/android.widget.RelativeLayout[last()]").click()
        return AddMemberPage(self._driver)

    def goto_pinfo(self, name):
        self.find_ele(MobileBy.XPATH, f"//*[@resource-id='com.tencent.wework:id/b0_']//*[@text={name}]").click()
        return PInfoPage(self._driver)
