# coding=utf-8
# auther:wangc
# 2020-05-19
from web.second_task.page.home_page import HomePage


class Test_Add_Member:

    def setup(self):
        self.home = HomePage()

    def test_addmember(self):
        self.contracts = self.home.goto_contracts()
        self.contracts.add_member()
        names = self.contracts.get_member_names()
        assert 'aaa' in names

    def teardown(self):
        self.contracts.delete_member('aaa')
        self.contracts.quit_chrome()