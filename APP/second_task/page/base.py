# coding=utf-8
# auther:wangc
# 2020-05-26
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None

    def __init__(self, driver=None):
        if driver:
            self._driver = driver
        else:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)

    def find_ele(self, by, locator):
        return self._driver.find_element(by, locator)

    def find_eles(self, by, locator):
        return self._driver.find_elements(by, locator)

    def get_toast(self, toast_text=''):

        if toast_text:
            toast_loc = self._driver.find_elements(MobileBy.XPATH, f"//*[contains(@text,'{toast_text}')]")
        else:
            toast_loc = self._driver.find_elements(MobileBy.XPATH, f"//android.widget.Toast")

        WebDriverWait(self._driver, 6, 0.3).until(
            expected_conditions.presence_of_element_located((MobileBy.XPATH, toast_loc)))
        return True

    def quit_app(self):
        self._driver.quit()
