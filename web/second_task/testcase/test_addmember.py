# coding=utf-8
# auther:wangc
# 2020-05-19
from web.second_task.page.main_page import MainPage


class Test_Add_Member:

    def setup(self):
        self.home = MainPage()

    def test_addmember(self):
        self.contracts = self.home.goto_contracts()
        self.contracts.add_member()
        names = self.contracts.get_member_names()
        assert 'aaa' in names

    def teardown(self):
        self.contracts.delete_member('aaa')
        self.contracts.quit_chrome()
