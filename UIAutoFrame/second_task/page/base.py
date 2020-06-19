from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from UIAutoFrame.second_task.page.wrapper import handle_alert, print_log


class BasePage:


    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def set_implicitly_wait(self, time):
        self._driver.implicitly_wait(time)

    # 查找元素
    @handle_alert
    def find_ele(self, locator, value: str = None):

        # 判断传进来的locator是否是元组，如果是解元组，如果不是，使用locator, value两个参数定位
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    # 查找元素集
    @print_log
    def find_eles(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 滑动查找text属性是指定内容的元素
    @print_log
    def scroll_find(self, value):
        return self._driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(' + '"' + value + '"' + ').instance(0));')

    # 滑动查找text属性开头是指定内容的元素
    @print_log
    def scroll_find_start_text(self, value):
        return self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textStartsWith("{value}").instance(0));')

    # 返回上一步
    @print_log
    def go_back(self):
        self._driver.back()
        return self

    # 获取toast文本，并返回
    @print_log
    def get_toast(self, toast_text=''):

        if toast_text:
            toast_loc = (MobileBy.XPATH, f"//*[contains(@text,'{toast_text}')]")
        else:
            toast_loc = (MobileBy.XPATH, f"//android.widget.Toast")
        # b = self.find_ele(toast_loc).text
        toast_frame = WebDriverWait(self._driver, 5, 0.01).until(lambda x: self._driver.find_element(*toast_loc))
        return toast_frame.text
