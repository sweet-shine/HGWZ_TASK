# coding=utf-8
# auther:wangc
# 2020-05-19
from selenium.webdriver.common.by import By

from web.second_task.page.addmember_page import AddMemberPage
from web.second_task.page.base_page import BasePage
from web.second_task.page.contracts_page import ContractsPage


class MainPage(BasePage):
    # 访问企业微信首页
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addmember(self):
        '''
        点击首页的添加成员按钮，返回添加成员页面
        :return:
        '''
        self.find_ele(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self._driver)

    def goto_contracts(self):
        '''
        点击通讯录按钮，返回通讯录页面
        :return:
        '''
        self.find_ele(By.ID, 'menu_contacts').click()
        return ContractsPage(self._driver)
