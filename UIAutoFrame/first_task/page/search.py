# coding=utf-8
# auther:wangc
# 2020-06-16
from appium.webdriver.common.mobileby import MobileBy

from UIAutoFrame.first_task.page.base import BasePage


class Search_Page(BasePage):
    def search(self, text):
        self.find_ele(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(text)
        # self.find_ele(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').click()
        self.find_ele(MobileBy.XPATH, f"//androidx.recyclerview.widget.RecyclerView//*[@text='{text}']").click()
        self.find_ele(MobileBy.XPATH,
                      f"//*[contains(@resource-id,'ll_stock_item_container')]//*[@text='{text}']/../..//*[@text='加自选']").click()
        return self

    def is_choose(self, text):
        res_list = self.find_eles(MobileBy.XPATH,
                      f"//*[contains(@resource-id,'ll_stock_item_container')]//*[@text='{text}']/../..//*[@text='已添加']")
        print(len(res_list))
        return len(res_list)

