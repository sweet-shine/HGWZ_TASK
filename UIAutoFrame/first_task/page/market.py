# coding=utf-8
# auther:wangc
# 2020-06-16
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.first_task.page.base import BasePage
from UIAutoFrame.first_task.page.search import Search_Page


class Market_Page(BasePage):

    def goto_search(self):
        # self.find_ele(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        return Search_Page(self._driver)
