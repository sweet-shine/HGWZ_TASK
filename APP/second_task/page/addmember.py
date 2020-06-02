# coding=utf-8
# auther:wangc
# 2020-05-26
from appium.webdriver.common.mobileby import MobileBy

from APP.second_task.page.base import BasePage


class AddMemberPage(BasePage):

    def add_manully(self, name, sex='男', phone_num=''):
        # 点击手动添加按钮
        # com.tencent.wework:id/c7t
        self.find_ele(MobileBy.ID, 'com.tencent.wework:id/c7x').click()

        #输入姓名
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dwa']//android.widget.EditText").send_keys(name)
        #选择性别，如果性别是男，不做任何操作，直接填写下个字段。如果性别是女，则选择
        if sex == '女':
            self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/cmk']/android.widget.RelativeLayout").click()
            self.find_eles(MobileBy.ID, 'com.tencent.wework:id/drk')[-1].click()

        #输入手机号
        self.find_ele(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/e8_']//android.widget.EditText").send_keys(phone_num)

        #保存
        self.find_ele(MobileBy.ID, 'com.tencent.wework:id/gvy').click()

        return self

    # def get_toast(self, toast_text=''):
    #
    #     if toast_text:
    #         toast_loc = (MobileBy.XPATH, f"//*[contains(@text,'{toast_text}')]")
    #     else:
    #         toast_loc = (MobileBy.XPATH, f"//android.widget.Toast")
    #     b = self.find_ele(toast_loc).text
    #     # WebDriverWait(self._driver, 5, 0.1).until(
    #     #      expected_conditions.presence_of_element_located(toast_loc))
    #
    #     return b