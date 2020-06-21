import pytest
import yaml

from UIAutoFrame.second_task.page.app import APP


class Test_Search:

    def setup(self):
        self.app = APP()
        self.app.start_app()


    def teardown(self):
        self.app.stop_app()

    @pytest.mark.parametrize('stock_name', yaml.safe_load(open('../data/stock_name.yaml', encoding='utf-8')))
    def test_search(self, stock_name):
        self.search = self.app.goto_main().goto_market().goto_search().search(stock_name)
        if self.search.is_choose(stock_name):
            self.search.reset(stock_name)
        self.search.add(stock_name)
        assert self.search.is_choose(stock_name)
