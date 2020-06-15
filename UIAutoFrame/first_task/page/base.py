# coding=utf-8
# auther:wangc
# 2020-05-26

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _black_list = {'确定', '确认', '取消', '是', '下次再说'}
    _max_retry = 3
    _error_times = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 查找元素
    def find_ele(self, locator, value: str = None):

        try:
            # 判断传进来的locator是否是元组，如果是解元组，如果不是，使用locator, value两个参数定位
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)

            self._driver.implicitly_wait(5)
            return element

        # 如果未找到元素，则看看是否有需要处理的弹框
        except Exception as e:
            print(f'第{self._error_times}次没找到元素')
            # 每次找不到，错误次数就+1
            self._error_times += 1
            # 如果错误次数>最大重试次数，抛出异常
            if self._error_times > self._max_retry:
                raise e
            # 如果错误次数不够，则处理弹框
            self._driver.implicitly_wait(1)
            for _black_ele in self._black_list:
                print(f'查找名称包含{_black_ele}的弹窗')
                eles = self._driver.find_elements(MobileBy.XPATH, f"//*[contains(@text,'{_black_ele}')]")
                if len(eles) > 0:
                    eles[0].click()
                    return self.find_ele(locator, value)
            raise e

    # 查找元素集
    def find_eles(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 滑动查找text属性是指定内容的元素
    def scroll_find(self, value):
        return self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(' + '"' + value + '"' + ').instance(0));')

    # 滑动查找text属性开头是指定内容的元素
    def scroll_find_start_text(self, value):
        return self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textStartsWith("{value}").instance(0));')

    # 返回上一步
    def go_back(self):
        self._driver.back()
        return self

    # 获取toast文本，并返回
    def get_toast(self, toast_text=''):

        if toast_text:
            toast_loc = (MobileBy.XPATH, f"//*[contains(@text,'{toast_text}')]")
        else:
            toast_loc = (MobileBy.XPATH, f"//android.widget.Toast")
        # b = self.find_ele(toast_loc).text
        toast_frame = WebDriverWait(self._driver, 5, 0.01).until(lambda x: self._driver.find_element(*toast_loc))
        return toast_frame.text
