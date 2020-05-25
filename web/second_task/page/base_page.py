from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    '''
    类变量_driver、_base_url
    '''
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        '''
        如果传了driver，则用传的driver；如果没传，则使用复用的driver
        :param driver:
        '''
        if driver:
            self._driver = driver
        else:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)

        # 如果继承的类变量的_base_url不为空，则访问_base_url;如果未设置，则为空，不做操作
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find_ele(self, by, locator):
        '''
        查找单元素封装，两个参数，一个定位方法，一个定位语句
        :param by:
        :param locator:
        :return:
        '''
        return self._driver.find_element(by, locator)

    def find_eles(self, by, locator):
        '''
        查找多元素封装，两个参数，一个定位方法，一个定位语句
        :param by:
        :param locator:
        :return:
        '''
        return self._driver.find_elements(by, locator)

    def quit_chrome(self):
        # 退出driver
        self._driver.quit()
