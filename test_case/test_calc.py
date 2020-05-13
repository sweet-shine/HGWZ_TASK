import pytest
import yaml
from python_task.calc import Calc
from decimal import Decimal


class Test_Calc:

    @pytest.mark.parametrize("a,b,exp", yaml.safe_load(open('../datas/test_calc_add_data.yml')))
    def test_add(self, a, b, exp):
        self.calc = Calc()
        res = self.calc.add(a, b)
        print(a, b, res, exp)
        assert res == exp

    @pytest.mark.parametrize("a,b,exp", yaml.safe_load(open('../datas/test_calc_div_data.yml')))
    def test_div(self, a, b, exp):

        if b == 0:
            pytest.xfail("除数不能为0")
        else:
            self.calc = Calc()
            res = self.calc.div(a, b)
            print(a, b, res, exp)
            assert res == exp


if __name__ == '__main__':
    pytest.main()
