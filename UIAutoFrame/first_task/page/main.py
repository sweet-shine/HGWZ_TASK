# coding=utf-8
# auther:wangc
# 2020-06-16
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.first_task.page.base import BasePage
from UIAutoFrame.first_task.page.market import Market_Page


class Main_Page(BasePage):

    def goto_market(self):
        self.find_ele(MobileBy.XPATH, "//android.widget.TabHost//*[@text='行情']").click()
        return Market_Page(self._driver)
