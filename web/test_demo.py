# coding=utf-8
# auther:wangc
# 2020-05-22
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_demo():
    options = Options()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)

    driver.find_element(By.ID, 'menu_contacts').click()
    time.sleep(2)
    #//*[@id="js_contacts25"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]
    eles = driver.find_elements(By.XPATH, "//*[@class='ww_operationBar']/a[1]")
    print(eles)
    print(len(eles))
    driver.find_element(By.XPATH, "//*[@class='ww_operationBar']/a[1]").click()
    time.sleep(3)
    driver.find_element_by_class_name('js_mod_party_name').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.ww_operationBar>.js_import_other_wrap').click()
    time.sleep(2)
    driver.find_element_by_class_name('frame_nav_item').click()
    time.sleep(2)

    driver.quit()
