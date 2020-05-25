# coding=utf-8
# auther:wangc
# 2020-05-19
from web.second_task.page.main_page import MainPage


class Test_Add_Member:

    def setup(self):
        '''
        初始化首页对象
        :return:
        '''
        self.home = MainPage()

    def test_addmember(self):
        '''
        先进入通讯录页面，再点击添加成员按钮，添加成员，并判断是否添加成功
        :return:
        '''
        self.contracts = self.home.goto_contracts()
        self.contracts.goto_addmember().add_member()

        names = self.contracts.get_member_names()
        assert 'aaa' in names

    def teardown(self):
        '''
        数据清除，删除本次添加的成员，退出driver
        :return:
        '''
        self.contracts.delete_member('aaa')
        self.contracts.quit_chrome()
