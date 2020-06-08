# coding=utf-8
# auther:wangc
# 2020-05-26
import pytest
import yaml

from APP.second_task.page.app import APP


class Test_Add_Manully:

    def setup(self):
        self.app = APP().start_app()

    def teardown(self):
        self.app.stop_app()

    @pytest.mark.parametrize(["name", "sex", "phone_num"],
                             yaml.safe_load(open('../data/mem_data.yml', encoding='utf-8'))['add_data'])
    def test_add_manully(self, name, sex, phone_num):
        res = self.app.goto_main().goto_contracts().goto_addmember().add_manully(name, sex, phone_num).get_toast('添加成功')
        print(res)
        assert '添加成功' in res
        self.app.goto_main()
