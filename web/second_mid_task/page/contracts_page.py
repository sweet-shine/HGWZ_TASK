# coding=utf-8
# auther:wangc
# 2020-05-19
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ContractsPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
        sleep(2)
        self._driver.find_element(By.ID, 'username').send_keys('aaa')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('aaa')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self._driver.find_element(By.CLASS_NAME, 'js_btn_save').send_keys('11111111111')

    def get_member_names(self):
        sleep(2)
        members = self._driver.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        names = [member.text for member in members]
        return names

    def quit_chrome(self):
        self._driver.quit()
