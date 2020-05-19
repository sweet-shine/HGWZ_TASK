# coding=utf-8
# auther:wangc
# 2020-05-19
from web.second_mid_task.page.home_page import HomePage


class Test_Add_Member:

    def setup(self):
        self.home = HomePage()

    def test_addmenber(self):
        self.contracts = self.home.goto_contracts()
        self.contracts.add_member()
        names = self.contracts.get_member_names()
        assert 'aaa' in names

    def teardown(self):
        self.contracts.quit_chrome()