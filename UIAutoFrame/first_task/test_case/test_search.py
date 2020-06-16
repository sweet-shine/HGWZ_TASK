# coding=utf-8
# auther:wangc
# 2020-06-16
from UIAutoFrame.first_task.page.app import APP


class Test_Search:

    def setup(self):
        self.search = APP().start_app().goto_main().goto_market().goto_search().search('阿里巴巴')

    def teardown(self):
        pass

    def test_search(self):
        assert self.search.is_choose('阿里巴巴')
