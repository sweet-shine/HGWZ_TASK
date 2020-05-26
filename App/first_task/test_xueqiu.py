from appium import webdriver


# com.xueqiu.android/.view.WelcomeActivityAlias
class Test_XueQiu:
    def setup(self):

        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['noReset'] = "true"
        caps['skipServerInstallation'] = True
        caps['skipDeviceInitialization'] = True

        self.driver = webdriver.Remote("http://localhost:4724/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_xueqiu(self):
        el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        el3 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        el3.click()
        el4 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.TextView")
        el4.click()
        el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_left")
        el5.click()
        el6 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
        el6.click()
        el7 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el7.click()
        el8 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el8.click()
        el8.send_keys("xiaomi")
        el9 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        el9.click()
        el10 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
        el10.click()

    def teardown(self):
        self.driver.quit()