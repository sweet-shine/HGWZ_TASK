# coding=utf-8
# auther:wangc
# 2020-05-19
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

from web.second_task.page.contracts_page import ContractsPage


class HomePage:

    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self._driver = webdriver.Chrome(options=options)

    def goto_contracts(self):
        self._driver.find_element(By.ID, 'menu_contacts').click()
        return ContractsPage(self._driver)
