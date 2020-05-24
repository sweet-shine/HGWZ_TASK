# coding=utf-8
# auther:wangc
# 2020-05-19
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

from web.second_task.page.base_page import BasePage
from web.second_task.page.contracts_page import ContractsPage


class MainPage(BasePage):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addmember(self):
        self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return ContractsPage(self._driver)

    def goto_contracts(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return ContractsPage(self._driver)
