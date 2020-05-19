import shelve
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

# 创建options参数
options = Options()
options.debugger_address = '127.0.0.1:9222'

# 复用浏览器
driver = webdriver.Chrome(options=options)

# 新建shelve文件，并保存复用浏览器的cookies
f = shelve.open('first_task/datas/cookies')
f['cookies'] = driver.get_cookies()
# 打印一下保存的cookies
print(f['cookies'])

# 关闭driver
driver.quit()


try:
    # 新建一个不使用复用浏览器的driver，并访问企业微信地址
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/frame')

    # 把刚才保存的cookies添加到当前企业微信页面的cookies中
    cookies = f['cookies']
    for cookie in cookies:

        if 'expiry' in cookie.keys():
            cookie.pop('expiry')
        driver.add_cookie(cookie)

    f.close()

    # 再次访问企业微信地址
    driver.get('https://work.weixin.qq.com/wework_admin/frame')

    # 点击通讯录按钮
    driver.find_element_by_id('menu_contacts').click()
    sleep(3)
finally:
    # 关闭driver
    driver.quit()
