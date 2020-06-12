import pytest
import yaml

from APP.second_task.page.app import APP


class Test_Del_Mem:

    def setup(self):
        self.app = APP().start_app()

    def teardown(self):
        self.app.stop_app()

    @pytest.mark.parametrize("name", yaml.safe_load(open('../data/mem_data.yml', encoding='utf-8'))['del_data'])
    def test_del_member(self, name):
        self.contract = self.app.goto_main().goto_contracts()
        pre_num = self.contract.get_members_num()
        print(pre_num)
        del_res = self.contract.goto_delmember().del_member(name)
        after_num = self.contract.get_members_num()
        print(after_num)
        assert pre_num - after_num == 1
