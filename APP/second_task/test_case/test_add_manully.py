# coding=utf-8
# auther:wangc
# 2020-05-26
from APP.second_task.page.app import APP


class Test_Add_Manully:

    def setup_class(self):
        self.app = APP().start_app()

    def teardown_class(self):
        self.app.stop_app()

    def test_add_manully(self):
        res = self.app.goto_main().goto_contracts().goto_addmember().add_manully('aaa', '女', 11111111135).get_toast('添加成功')
        print(res)
        assert '添加成功' in res
