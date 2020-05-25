# coding=utf-8
# auther:wangc
# 2020-05-19
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from web.second_task.page.addmember_page import AddMemberPage
from web.second_task.page.base_page import BasePage


class ContractsPage(BasePage):

    def goto_addmember(self):
        '''
        点击添加成员按钮，返回添加成员页面
        :return:
        '''
        # 显示等待“添加成员”按钮，可点击
        add_member_locator = (By.CSS_SELECTOR, '.ww_operationBar>a.js_add_member')
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(add_member_locator))

        self.find_ele(*add_member_locator).click()
        return AddMemberPage(self._driver)

    def get_member_names(self):
        '''
        获取通讯录页面所有成员姓名，返回所有姓名list
        :return:
        '''
        # 显示等待姓名前面的复选框是否可点击，可点击了再获取所有姓名，以免姓名获取不全
        check_box_locator = (By.CLASS_NAME, 'ww_checkbox')
        WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(check_box_locator))

        members = self.find_eles(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        names = [member.text for member in members]
        return names

    def delete_member(self, name):
        '''
        删除成员，提供姓名参数
        :param name:
        :return:
        '''
        members_info = self.find_eles(By.ID, 'member_list')
        # members = self._driver.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        for member_info in members_info:
            member_name = member_info.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            member_checkbox = member_info.find_element(By.CSS_SELECTOR, 'td:nth-child(1)')
            if member_name == name:
                member_checkbox.click()
                self.find_ele(By.CLASS_NAME, 'js_delete').click()
                self.find_ele(By.CSS_SELECTOR, "a[d_ck='submit']").click()
        return self
