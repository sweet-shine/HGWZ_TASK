# coding=utf-8
# auther:wangc
# 2020-06-01
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from APP.second_task.page.base import BasePage


class PInfoPage(BasePage):

    def goto_info(self):
        # 点击右上角三个点的按钮
        self.find_ele()
        #点击编辑成员按钮
        self.find_ele(MobileBy.ID,'com.tencent.wework:id/azn').click()
        self.find_ele()
