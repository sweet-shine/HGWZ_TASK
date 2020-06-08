from appium.webdriver.common.mobileby import MobileBy
from APP.second_task.page.base import BasePage


class DelMemberPage(BasePage):

    def del_member(self, name):
        # 点击对应的姓名
        self.find_ele(MobileBy.XPATH,
                      f'//android.widget.RelativeLayout//android.widget.TextView[@text="{name}"]').click()
        # 点击右上角三个点的按钮
        self.find_eles(MobileBy.XPATH,
                       "//android.widget.TextView[@text='个人信息']/../../../../..//android.widget.TextView")[-1].click()
        # 点击编辑成员按钮
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='编辑成员']").click()
        # 点击删除成员按钮
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='删除成员']").click()
        # 点击确定按钮
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='确定']").click()
