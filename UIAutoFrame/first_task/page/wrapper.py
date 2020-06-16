# coding=utf-8
# auther:wangc
# 2020-06-16

from appium.webdriver.common.mobileby import MobileBy


# 处理弹窗
def handle_alert(func):
    def wrapper(*args, **kwargs):
        from UIAutoFrame.first_task.page.base import BasePage
        _black_list = ['确定', '确认', '取消', '是', '下次再说']
        _error_num = 0
        _max_retry = 3

        instance: BasePage = args[0]

        try:
            element = func(*args, **kwargs)
            instance._driver.implicitly_wait(5)
            return element
        # 如果未找到元素，则看看是否有需要处理的弹框
        except Exception as e:
            # 每次找不到，错误次数就+1
            _error_num += 1
            print(f'第{_error_num}次没找到元素')
            # 如果错误次数>最大重试次数，抛出异常
            if _error_num >= _max_retry:
                raise e
            # 如果错误次数不够，则处理弹框
            instance._driver.implicitly_wait(1)
            for _black_ele in _black_list:
                print(f'查找名称包含{_black_ele}的弹窗')
                eles = instance._driver.find_elements(MobileBy.XPATH, f"//*[contains(@text,'{_black_ele}')]")
                if len(eles) > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)

    return wrapper
