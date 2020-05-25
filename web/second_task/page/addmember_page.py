# coding=utf-8
# auther:wangc
# 2020-05-25
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from web.second_task.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self):
        '''
        添加成员页面，必填字段：姓名、账号、手机号
        :return:
        '''
        self.find_ele(By.ID, 'username').send_keys('aaa')
        self.find_ele(By.ID, 'memberAdd_acctid').send_keys('aaa')
        self.find_ele(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self.find_ele(By.CLASS_NAME, 'js_btn_save').click()

        return self
