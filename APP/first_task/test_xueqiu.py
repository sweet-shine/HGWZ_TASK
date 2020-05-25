# coding=utf-8
# auther:wangc
# 2020-05-25

# com.xueqiu.android/.common.splash.SplashActivity
from appium import webdriver


def setup_class(self):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7',
        'deviceName': 'test',
        'appPackage': 'com.hjimi.cmpay',
        'appActivity': 'com.hjimi.cmpay.activity.SplashActivity',
        # 'appActivity': '.activity.MainActivity',
        'automationName': 'uiautomator2',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'newCommandTimeout': 6000
    }

    # 启动Remote RPC
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    self.driver.implicitly_wait(10)


def teardown_class(self):
    self.driver.quit()