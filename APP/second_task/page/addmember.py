# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.base import BasePage


class AddMemberPage(BasePage):

    def add_manully(self, name, sex='男', phone_num=''):
        # 点击手动添加按钮
        self.find_ele(MobileBy.ID, 'com.tencent.wework:id/c7t').click()

        #输入姓名
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dw2']//android.widget.EditText").send_keys(name)
        #选择性别，如果性别是男，不做任何操作，直接填写下个字段。如果性别是女，则选择
        if sex == '女':
            self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/cme']/android.widget.RelativeLayout").click()
            self.find_eles(MobileBy.ID, 'com.tencent.wework:id/b34')[-1].click()

        #输入手机号
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e81']//android.widget.EditText").send_keys(phone_num)

        #保存
        self.find_ele(MobileBy.ID, 'com.tencent.wework:id/gvk').click()

