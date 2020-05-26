# coding=utf-8
# auther:wangc
# 2020-05-26
from APP.second_task.page import main


class Test_Add_Manully:

    def setup_class(self):
        self.main = main.MainPage()

    def teardown_class(self):
        self.main.quit_app()

    def test_add_manully(self):
        self.main.goto_contracts().goto_addmember().add_manully('aaa', '女', 11111111118)
        assert self.main.get_toast('添加成功')
