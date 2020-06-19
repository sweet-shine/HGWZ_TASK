from UIAutoFrame.second_task.page.app import APP


class Test_Search:

    def setup(self):
        self.app = APP()
        self.app.start_app()


    def teardown(self):
        self.app.stop_app()

    def test_search(self):
        self.search = self.app.goto_main().goto_market().goto_search().search()
        if self.search.is_choose():
            self.search.reset()
        self.search.add()
        assert self.search.is_choose()
