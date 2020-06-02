# coding=utf-8
# auther:wangc
# 2020-05-26
from APP.second_task.page import main
from APP.second_task.page.addmember import AddMemberPage
from APP.second_task.page.app import APP


class Test_Add_Manully:

    def setup_class(self):
        self.app = APP().start_app()

    def teardown_class(self):
        self.app.stop_app()

    def test_add_manully(self):
        self.app.goto_main().goto_contracts().goto_addmember().add_manully('aaa', '女', 11111111128)
        self.invit = AddMemberPage()
        res = self.invit.get_toast()
        assert '成功' in res
