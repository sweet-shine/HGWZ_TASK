from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):

        if driver:
            self._driver = driver
        else:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)

        if self._base_url != "":
            self._driver.get(self._base_url)
