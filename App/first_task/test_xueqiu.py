import time

import pytest
from appium import webdriver


# com.xueqiu.android/.view.WelcomeActivityAlias
from appium.webdriver.common.mobileby import MobileBy


class Test_XueQiu:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        # time.sleep(10000)

    @pytest.mark.parametrize("serch_content,expect_content",
                             [('alibaba', '阿里巴巴'), ('xiaomi', '小米集团-W'), ('jingdong', '京东')])
    def test_xueqiu(self, serch_content, expect_content):
        # 点击搜索框
        el1 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        el1.click()

        # 输入待搜索的内容
        el2 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        el2.send_keys(serch_content)

        # 选择text为预期文字的元素
        el3 = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{expect_content}']")
        el3.click()

        # 点击加自选按钮
        el4 = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{expect_content}']/../..//*[@text='加自选']")
        el4.click()

        # 判断已添加状态
        el5 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{expect_content}']/../..//*[@text='已添加']")
        assert len(el5) >= 1

        # 将已添加状态重置为未添加状态
        el4 = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{expect_content}']/../..//*[@text='已添加']")
        el4.click()

    def teardown(self):
        # 点击取消按钮
        el6 = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close")
        el6.click()

    def teardown_class(self):
        self.driver.quit()
