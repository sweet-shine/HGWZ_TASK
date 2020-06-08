# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.base import BasePage


class AddMemberPage(BasePage):

    def add_manully(self, name, sex='男', phone_num=''):
        # 点击手动添加按钮
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='手动输入添加']").click()
        #输入姓名
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='姓名　']/../android.widget.EditText").send_keys(name)

        #选择性别，如果性别是男，不做任何操作，直接填写下个字段。如果性别是女，则选择
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='性别']/../android.widget.RelativeLayout").click()
        if sex == '女':
            self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='女']").click()
        else:
            self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='男']").click()

        #输入手机号
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='手机　']/..//android.widget.EditText").send_keys(phone_num)

        #保存
        self.find_ele(MobileBy.XPATH, "//android.widget.TextView[@text='保存']").click()

        return self