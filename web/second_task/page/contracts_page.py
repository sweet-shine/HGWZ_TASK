# coding=utf-8
# auther:wangc
# 2020-05-19
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from web.second_task.page.base_page import BasePage


class ContractsPage(BasePage):

    def add_member(self):
        add_member_locator = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        ele = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(add_member_locator))
        print(ele)
        print(type(ele))
        # print(*add_member_locator)
        # sleep(2)
        self._driver.find_element(*add_member_locator).click()
        # ele.click()
        sleep(2)
        self._driver.find_element(By.ID, 'username').send_keys('aaa')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('aaa')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self._driver.find_element(By.CLASS_NAME, 'js_btn_save').click()

    def get_member_names(self):
        sleep(2)
        members = self._driver.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        names = [member.text for member in members]
        return names

    def delete_member(self, name):
        members_info = self._driver.find_elements(By.ID, 'member_list')
        # members = self._driver.find_elements(By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        for member_info in members_info:
            member_name = member_info.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
            member_checkbox = member_info.find_element(By.CSS_SELECTOR, 'td:nth-child(1)')
            if member_name == name:
                member_checkbox.click()
                self._driver.find_element(By.CLASS_NAME, 'js_delete').click()
                self._driver.find_element(By.CSS_SELECTOR, "a[d_ck='submit']").click()

    def quit_chrome(self):
        self._driver.quit()
