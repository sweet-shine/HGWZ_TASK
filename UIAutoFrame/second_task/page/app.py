from appium import webdriver
from UIAutoFrame.second_task.page.base import BasePage
from UIAutoFrame.second_task.page.main import Main_Page


class APP(BasePage):

    def start_app(self):
        if self._driver:
            self._driver.launch_app()
        else:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["automationName"] = "uiautomator2"
            caps['noReset'] = "true"
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        self._driver.implicitly_wait(5)

        return self

    def stop_app(self):
        self._driver.quit()

    def restart_app(self):
        pass

    def goto_main(self) -> Main_Page:
        return Main_Page(self._driver)
