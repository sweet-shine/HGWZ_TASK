
from APP.second_task.page.app import APP


class Test_Del_Mem:

    def setup_class(self):
        self.app = APP().start_app()

    def teardown_class(self):
        self.app.stop_app()

    def test_del_member(self):
        num = self.app.goto_main().goto_contracts().get_members_num()
        print(num)